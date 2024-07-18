'''
This modul create a app instanze of flask and starts it if run as __main__.

The app has two routes index and emotionDetector
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Instantiate Flask functionality
app = Flask(__name__)

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    result = emotion_detector(text_to_analyze)

    if not result['dominant_emotion']:
        return 'Invalid text! Please try again!.'

    response = f"""
                For the given statement, the system response is:
                'anger': {result['anger']},
                'disgust': {result['disgust']},
                'fear': {result['fear']},
                'joy': {result['joy']},
                'sadness': {result['sadness']}.
                The dominant emotion is {result['dominant_emotion']}.
                """

    return response

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)

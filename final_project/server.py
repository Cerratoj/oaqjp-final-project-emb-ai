from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_Detectors():
    emotion_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(emotion_to_analyze)
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']

    list_of_response = {
        'anger': response['anger'], 
        'disgust': response['disgust'], 
        'fear': response['fear'], 
        'joy': response['joy'], 
        'sadness': response['sadness']
        }
    name_of_dominant_response = max(list_of_response, key=list_of_response.get)  

    return "For the given statement, the system response is {}. The dominant emotion is {}.".format(list_of_response, name_of_dominant_response)
    
@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


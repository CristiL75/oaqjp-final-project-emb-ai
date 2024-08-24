"""
server.py

This module defines a Flask application with a single endpoint that processes
text input to detect emotions using the emotion_detector function from the
emotion_detection module.
"""

from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotion_detector', methods=['POST'])
def emotion_detector_endpoint():
    """
    Handles the /emotion_detector endpoint.

    Expects a JSON payload with a 'text' field. 
    Returns the emotion analysis of the provided text.
    If no valid text is provided, returns an error message.

    Returns:
        Response object with JSON data and HTTP status code.
    """
    data = request.get_json()
    text_to_analyze = data.get('text', '')
    result = emotion_detector(text_to_analyze)
    
    if result['dominant_emotion'] is None:
        # Return an error message for invalid or blank text
        return jsonify({'error': 'Invalid text! Please try again!'}), 400
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

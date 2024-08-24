import requests

def emotion_detector(text_to_analyze):
    # Define the URL and headers
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    # Check for blank input
    if not text_to_analyze.strip():
        # Return a dictionary with None values for blank input
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    
    try:
        # Prepare the input JSON
        input_json = {
            "raw_document": {
                "text": text_to_analyze
            }
        }

        # Make the POST request to the API
        response = requests.post(url, json=input_json, headers=headers)
        
        # Raise an exception for HTTP errors
        response.raise_for_status()
        
        # Parse and handle the response
        response_data = response.json()

        # Extract emotions
        emotions = response_data.get('emotionPredictions', [{}])[0].get('emotion', {})
        
        # Determine the dominant emotion
        dominant_emotion = max(emotions, key=emotions.get, default=None)
        
        # Return formatted results
        return {
            "anger": emotions.get('anger'),
            "disgust": emotions.get('disgust'),
            "fear": emotions.get('fear'),
            "joy": emotions.get('joy'),
            "sadness": emotions.get('sadness'),
            "dominant_emotion": dominant_emotion
        }
        
    except requests.exceptions.RequestException as e:
        # Handle exceptions during the request
        print(f"An error occurred: {e}")
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

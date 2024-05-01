import paralleldots
import os
api = os.getenv('parallel_dots_api')
paralleldots.set_api_key(api)

def ner(text):
    ner = paralleldots.ner(text)
    return ner

def sentiment_analysis(text):
    lang_code="en"
    response=paralleldots.sentiment(text,lang_code)
    return response

def abuse_detection(text):
    
    response = paralleldots.abuse(text)
    return response
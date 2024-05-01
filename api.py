import paralleldots
paralleldots.set_api_key('yQebaEl2kQJGfZv9kKvosLSmDF5gobr4os4BXt9fQlA')

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
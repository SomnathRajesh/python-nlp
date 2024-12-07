from textblob import TextBlob
import wikipedia
import nltk
nltk.download('punkt_tab')


def search_wikipedia(name):
    """Search wikipedia"""
    return wikipedia.search(name)

def summarize_wikipedia(name):
    """Summarize wikipedia"""
    return wikipedia.summary(name)

def get_text_blob(text):
    """Get text blob"""

    blob = TextBlob(text)
    return blob 

def get_phrases(name):
    """Find wiki name and return back phrases"""

    text = summarize_wikipedia(name)
    blob = get_text_blob(text)
    phrases = blob.noun_phrases
    return phrases


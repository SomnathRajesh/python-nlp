from nlplogic.corenlp import search_wikipedia,summarize_wikipedia,get_text_blob,get_phrases

def test_get_phrase():
    assert 'ipl' in get_phrases("Chennai Super Kings")
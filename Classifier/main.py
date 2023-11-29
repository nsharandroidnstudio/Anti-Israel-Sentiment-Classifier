from typing import List
from classifier import AntiIsraelClassifier
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
classifier = AntiIsraelClassifier()

class One_Sentence(BaseModel):
    sentence: str

class Multiple_Sentnces(BaseModel):
    list_of_sentences: List[str]

@app.post("/AntiIsraelClassifier/OneSentence", response_model=dict)
def classify_sentence(one_sentence:One_Sentence):
    """
    Classify the sentiment of the given sentence.

    Args:
        request (SentenceRequest): Request model containing the sentence to be classified.

    Returns:
        dict: JSON response containing the classification result.
    """
    # Check if the parameter named Text_data exists
    if one_sentence.sentence is None:
        return {"sentence": "parameter is required."}

    text_data = one_sentence.Text_data
    is_anti_israel = classifier.classify_Is_it_anti_pro_isreali(text_data)
    return {"sentence":text_data,"Is it anti israeli": is_anti_israel}

@app.post("/AntiIsraelClassifier/MultipleSentences", response_model=list[dict])
def classify_multiple_sentences(Multiple_Sentence: Multiple_Sentnces):
    """
    Classify the sentiment of multiple sentences.

    Args:
        request (SentencesRequest): Request model containing a list of sentences to be classified.

    Returns:
        List[dict]: A list of JSON responses containing the classification results for each sentence.
    """
    # Check if the parameter named list_of_sentences exists
    if not Multiple_Sentence.list_of_sentences:
        return {"error": "sentence parameter is required and must be a list of sentences."}

    sentences = Multiple_Sentence.list_of_sentences
    classification_responses = []
    for sentence in sentences:
        is_anti_israel = classifier.classify_Is_it_anti_pro_isreali(sentence)
        classification_responses.append({"Sentence": sentence, "Is it anti israeli": is_anti_israel})

    return classification_responses


@app.post("/Scoring_Anti_pro_isreali/MultipleSentences", response_model=list[dict])
def Scoring_multiple_sentences(Multiple_Sentence: Multiple_Sentnces):
    """
    Score multiple sentences.

    Args:
        multiple_sentences (Multiple_Sentences): Request model containing a list of sentences to be scored.
        content_type (str): Header parameter.

    Returns:
        dict: JSON response containing the scoring results.
    """
    if not Multiple_Sentence.list_of_sentences:
        return {"error": "sentence parameter is required and must be a list of sentences."}

    sentences = Multiple_Sentence.list_of_sentences
    classification_responses = []
    for sentence in sentences:
        score = classifier.Scoring_Scale_anti_pro_isreali(sentence)
        key, score = score.split(':')

        classification_responses.append({"Sentence": sentence, "score":score})

    return classification_responses


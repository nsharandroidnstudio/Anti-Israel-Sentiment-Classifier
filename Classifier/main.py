from typing import List
from classifier import AntiIsraelClassifierModelSetFit
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
classifierSetfit = AntiIsraelClassifierModelSetFit()
class One_Sentence(BaseModel):
    sentence: str

class Multiple_Sentnces(BaseModel):
    list_of_sentences: List[str]

from fastapi import HTTPException

@app.post("/AntiIsraelClassifier/OneSentence", response_model=dict)
def classify_sentence(one_sentence: One_Sentence):
    """
    Classify the sentiment of the given sentence.

    Args:
        one_sentence (One_Sentence): Request model containing the sentence to be classified.

    Returns:
        dict: JSON response containing the classification result.
    """
    try:
        # Check if the parameter named Text_data exists
        if one_sentence.sentence is None:
            raise HTTPException(status_code=400, detail="Sentence parameter is required.")

        text_data = one_sentence.sentence
        is_anti_israel,probability = classifierSetfit.classify_Is_it_anti_pro_isreali(text_data)
        return {
        "sentence": text_data,
        "is_anti_israel": is_anti_israel,
        "probability": probability
    }
    except Exception as e:
        return {"error": str(e)}


@app.post("/AntiIsraelClassifier/MultipleSentences", response_model=list[dict])
def classify_multiple_sentences(Multiple_Sentence: Multiple_Sentnces):
    """
    Classify the sentiment of multiple sentences.

    Args:
        Multiple_Sentence (Multiple_Sentences): Request model containing a list of sentences to be classified.

    Returns:
        List[dict]: A list of JSON responses containing the classification results for each sentence.
    """
    try:
        if not Multiple_Sentence.list_of_sentences:
            raise HTTPException(status_code=400, detail="Sentence parameter is required and must be a list of sentences.")

        sentences = Multiple_Sentence.list_of_sentences
        classification_responses = []
        for sentence in sentences:
            is_anti_israel,probability = classifierSetfit.classify_Is_it_anti_pro_isreali(sentence)
            classification_responses.append({
            "Sentence": sentence,
            "Is it anti-Israeli": is_anti_israel,
            "Probability": probability
            })

        return classification_responses

    except Exception as e:
        return {"error": str(e)}


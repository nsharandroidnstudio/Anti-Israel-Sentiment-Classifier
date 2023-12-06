import torch
from setfit import SetFitModel

class AntiIsraelClassifierModelSetFit:
        
        def __init__(self, model_path= "SavedModel\\model.joblib"):

            self.model = SetFitModel._from_pretrained(model_path)

        def classify_Is_it_anti_pro_isreali(self, sentence: str) -> bool:
            """
            Classifies the given sentence as anti-Israeli or pro-Israeli.

            Args:
            sentence (str): The sentence to be classified.

            Returns:
            bool: True if the sentence is classified as anti-Israeli, False otherwise.
            """
            import numpy as np
            prediction = self.model.predict([sentence])
            probabilities = self.model.predict_proba([sentence])
            probabilities_index = torch.argmax(probabilities)
            predicted_class_probability = probabilities[0, probabilities_index]
           
            if int(prediction) == 0:
                 return True,predicted_class_probability.item()
            return False,predicted_class_probability.item()

    
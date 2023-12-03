from gpt4all import GPT4All

class AntiIsraelClassifier:
    """
    A class for classifying sentences as anti-Israeli or pro-Israeli using GPT-4.

    Args:
        model_path (str): The path to the GPT-4 model.
    """

    def __init__(self, model_path= "mistral-7b-instruct-v0.1.Q4_0.gguf",temp=0.5):
        self.model = GPT4All(model_path)
        self.temp = temp

    def classify_Is_it_anti_pro_isreali(self, sentence: str) -> bool:
        """
        Classifies the given sentence as anti-Israeli or pro-Israeli.

        Args:
            sentence (str): The sentence to be classified.

        Returns:
            bool: True if the sentence is classified as anti-Israeli, False otherwise.
        """
        input_prompt = (
    "Task:Sentiment classification Classes:pro israeli,anti Israeli\n"
    "Context:Classify text as pro or anti-Israeli based on tone,context,and language cues.Adhere strictly to explicit content,avoiding assumptions or interpretations.Maintain neutrality,provide factual analysis,and refrain from offering opinions,political insights,or historical context. In ambiguous cases,note uncertainty make an arbitrary classification."
    "Examples:\n"
    "Text:From the river to the sea, Palestine will be free.\n"
    "Label:anti Israeli\n"
    "Text:I stand with isreal\n"
    "Label:pro isreali\n"
    "Text:hamas=isis\n"
    "Label:pro israeli"
    "Analyze sentiment in the text.\n"
    f"text:'{sentence}'\n"
)

        output = self.model.generate(input_prompt, max_tokens=14, temp=self.temp)
        return "anti" in output.lower()

    
    def Scoring_Scale_anti_pro_isreali(self, sentence: str) -> str:
            
            """
            Assigns a sentiment score on the anti-Israel to pro-Israel scale for the given sentence.

            Args:
            sentence (str): The input sentence for sentiment analysis.

             Returns:
            float: A sentiment score on the scale of -1 (indicating anti-Israel sentiment)to 1(indicating pro-Israel sentiment).
            """
            input_prompt = (
    "Task:Sentiment scoring\n"
    "Context:Score a sentence's sentiment on a scale from -1(anti-Israel)to 1(pro-Israel)considering tone,context,and language cues.\n"
    "Examples:\n"
    "Text:I Stand with Israel.\n"
    "Score:1\n"
    "Text:hamas=isis\n"
    "Score:0.9\n"
    "Text:stop antisemitism\n"
    "Score:0.8\n"
    "Israel is doing a genocide to the Palestinian\n"
    "Score:-1"
    "Text:Stop isreal occupation they making a PROPAGANDA\n"
    "Score:-0.8\n"
    "Text:From the river to the sea Palestinian will be free\n"
    "Score:-1\n"
    "give a score for the text.\n"
    f"text:{sentence}\n"
)
   

            output = self.model.generate(input_prompt, max_tokens=14, temp=self.temp)
            return output
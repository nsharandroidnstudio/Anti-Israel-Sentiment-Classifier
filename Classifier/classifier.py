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
    "Task: Sentiment classification\n"
    "Classes: pro israeli, anti Israeli\n"
    "Context: You are designed to classify texts as either pro or anti Israeli. Your primary role is to analyze the tone, context, and language cues within a given text to determine its alignment. You will strictly adhere to the content of the text and avoid making assumptions or interpretations that extend beyond the explicit content. You will not provide opinions, political insights, or historical context, ensuring neutrality and factual analysis. In cases where the text is ambiguous or lacks clear indicators, you will state the uncertainty and refrain from arbitrary classification.\n"
    "Labeled Examples:\n"
    "Text: I Stand with Israel.\n"
    "Label: pro israeli\n"
    "Text: From the river to the sea, Palestine will be free.\n"
    "Label: anti Israeli\n"
    "Text: I love isreal!\n"
    "Label pro isreali\n"
    "Text: Critics argue that Israel's military actions disproportionately affect civilian populations.\n"
    "Label: anti Israeli\n"
    "Text: The Israeli Defense Forces (IDF) play a crucial role in ensuring national security, demonstrating a commitment to safeguarding the nation and its people.\n"
    "Label: pro israeli\n"
    "Text: Fuck gaza\n"
    "Label: pro israeli"
    "Please classify the sentiment of the following text:\n"
    f"Sentence: '{sentence}'\n"
)

        output = self.model.generate(input_prompt, max_tokens=20, temp=self.temp)
        return "anti" in output.lower()

    
    def Scoring_Scale_anti_pro_isreali(self, sentence: str) -> str:
            
            """
            Assigns a sentiment score on the anti-Israel to pro-Israel scale for the given sentence.

            Args:
            sentence (str): The input sentence for sentiment analysis.

             Returns:
            float: A sentiment score on the scale of -1 (indicating anti-Israel sentiment) to 1 (indicating pro-Israel sentiment).
            """
            input_prompt = (
    "Task: Anti-Israeli Sentiment Scoring\n"
    "Scoring Scale: -1 (Anti-Israel) to 1 (Pro-Israel)\n"
    "Context: Provide a sentiment score for the given sentence, indicating the degree of anti-Israeli sentiment.Use a numerical scale where -1 represents anti-Israel sentiment, 0 is neutral, and 1 represents pro-Israel sentiment.\n"
    "Scoring Examples:\n"
    "Text: I Stand with Israel.\n"
     "Score:0.99\n"
    "Text: From the river to the sea, Palestine will be free.\n"
    "Score:-0.99\n"
    "Text: Critics argue that Israel's military actions disproportionately affect civilian populations.\n"
    "Score:-0.9\n"
    "Text: The Israeli Defense Forces (IDF) play a crucial role in ensuring national security, demonstrating a commitment to safeguarding the nation and its people.\n"
    "Score:0.9\n"
    "Text: stop antisemitism"
    "Score: 0.8"
    "Text: Fuck gaza\n"
    "Score:0.1\n"
    "Text: I believe in Israel's right to exist and defend its borders against external threats.\n"
    "Score:0.5"
    "Score:The hostage deal must include the realse of isreali woman and children had by hamash and the realse of palstininen women and children that isreal snatch\n"
    "Score:-0.6\n"
    "The hostage deal must include the release of Israeli women and children held by Hamas and the release of Palestinian women and children that Israel has holds\n"
    "Score:0.3\n"
    "Israel is doing a genocide to the Palestinian\n"
    "Score:-0.95"
    "Please Give a sentiment score following text:\n"
    f"Sentence: {sentence}\n"
)
   

            output = self.model.generate(input_prompt, max_tokens=20, temp=self.temp)
            return output
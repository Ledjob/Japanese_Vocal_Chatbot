from dotenv.main import load_dotenv
import os
from papago import Translator

load_dotenv()

CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET= os.environ['CLIENT_SECRET'] 


translator = Translator(CLIENT_ID, CLIENT_SECRET)

def english_trans(sentence):
    response = translator.translate(sentence, 'ja', 'en')
    return response

if __name__ == "__main__":
    sentence_to_translate = "Hello, how are you?"
    translated_text = english_trans(sentence_to_translate)
    print("Original:", sentence_to_translate)
    print("Translated:", translated_text)
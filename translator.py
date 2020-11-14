
#print(googletrans.LANGUAGES) # show languages
import googletrans
from googletrans import Translator

translator = Translator()

src_lang = input("Language to be Translated: ")
dest_lang = input("Destination Language: ")
text = input("Enter Text: ")
result = translator.translate(text, src=src_lang, dest=dest_lang)

#print(result) #src, dest, origin, text, pronounciation
print(result.text)

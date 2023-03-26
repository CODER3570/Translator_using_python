#Translate
from translate import Translator
translator = Translator(to_lang='ja')
try:
    with open('test.txt', 'r') as f:
        trans_file = f.read()
    translated_text = translator.translate(trans_file)
    #Create a new python file which is translated
    with open('text.txt', mode='w', encoding='utf-8') as myfile:
        myfile.write(translated_text)

except UnicodeEncodeError:
    print("o paii Error agya ee")


from googletrans import Translator

def Translate(txt,des=""):
    translator = Translator()
    if des == 'uz':
        return translator.translate(f"{txt}",dest='en').text
    else:
        return translator.translate(f"{txt}",dest='uz').text

from googletrans import Translator

def dichVanBan (text, target_language):
    translator = Translator()
    # origin_language = translator.detect(text)
    translated = translator.translate(text, dest=target_language)
    # print(origin_language.lang)
    return translated.text

def dichVanBan2 (text, old_language,target_language):
    translator = Translator()
    # origin_language = translator.detect(text)
    translated = translator.translate(text, src=old_language, dest=target_language)
    # print(origin_language.lang)
    return translated.text

# textInput = input("Text: ")
# languageTarget = input("Target language: ")
# print(dichVanBan(textInput, languageTarget))

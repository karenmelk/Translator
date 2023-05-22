from mtranslate import translate

# Set the text to be translated and the target language
# text = input("Please enter text -- > ")
# target_lang = "hy" # Spanish
target_lang = "en" 

# Translate the text
while True:
    text = input("Please enter text -- > ")
    if text == ' ':
        break
    else:
        translated_text = translate(text, target_lang)

# Print the translated text
        print(translated_text)

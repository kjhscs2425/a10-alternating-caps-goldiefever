
def sarcastic_text(text):
        text = text.replace("a", "A")
        text = text.replace("e", "E")
        text = text.replace("i", "I")
        text = text.replace("o", "O")
        text = text.replace("u", "U")
        return text

def aLtErNaTiNgCaPs():
    text = input("what would you like me to say sarcastically? \n")
    print(sarcastic_text(text))

aLtErNaTiNgCaPs()
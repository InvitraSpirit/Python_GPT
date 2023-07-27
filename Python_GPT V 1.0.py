question = input("olá! como posso te ajudar")
empty_list = []
words = ""
wrd_space = " "
phrase = []

for i in question:
    empty_list.append(i)
empty_list.append(" ")

for i in empty_list:
    if i != wrd_space: 
        words += i
    else:
        phrase.append(words)
        words = ""
    
print(phrase)
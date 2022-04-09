import re

sentence = input()
special_word = input()
pattern = rf"{special_word}"

result = re.findall(sentence, pattern, re.IGNORECASE)

print(len(result))

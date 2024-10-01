import re
pattern = r"[a-z]+at"
text = "The cat is in the hat."

matches = re.findall(pattern, text)
print(matches)

new_text = re.sub(pattern, "dog", text)
print(new_text)

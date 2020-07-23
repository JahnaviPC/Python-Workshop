Write python program to have a list of words to sort them from shortest to longest using list of tuples

txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for word in words:
   t.append((len(word), word))
t.sort(reverse=True)

res = list()
for length, word in t:
    res.append(word)

print(res)

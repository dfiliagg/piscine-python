def ft_split(string):
    lista = []
    word = ""
    for i in range(len(string)):
        if string[i] != " " and string[i] != "\n":
            word += string[i]
        else:
            if word != "":
                lista.append(word)
            word = ""
    if word != "":
        lista.append(word)
    return lista

def ft_sort(lista):
  for i in range(len(lista) - 1):
    for j in range(len(lista) - i - 1):
      if lista[j] > lista[j + 1]:
        lista[j], lista[j + 1] = lista[j + 1], lista[j]
  return lista

n = int(input("Insert an integer: "))
file = open("words.txt", "r")
text = file.read()
file.close()
words = ft_split(text)
lista = words[:]

for word in words:
    if len(word) <= n:
        lista.remove(word)

lista = ft_sort(lista)

file = open("long_words.txt", "w")
print(f'The words longer than {n} have been written on "long_words.txt"')
for word in lista:
    file.write(word+"\n")

file.close()

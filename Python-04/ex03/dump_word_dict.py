import pickle

def del_zero(diz):
    dic = dict(diz)
    for i in dic:
        if dic[i] == 0:
            del diz[i]

def create_dic(f):
    diz = {}
    max = -1
    for riga in f:
        if len(riga) > max:
            max = len(riga)
    for i in range(max):
        diz[i] = 0
    return diz

    
with open('words.txt', 'r') as f:
    diz = create_dic(f)
    f.seek(0)
    for riga in f:
        diz[len(riga)-1] += 1
    del_zero(diz)

with open("word_count.pickle", "wb") as f:
    f.write(pickle.dumps(diz))

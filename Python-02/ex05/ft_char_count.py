import sys

def ft_sorted(list):
    for i in range(len(list)):
        for j in range(len(list) - i - 1):
            if list[j][1] < list[j+1][1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

if len(sys.argv) < 2:
    print("Error! No string given")
    exit()
dic = {}
for c in sys.argv[1]:
	dic[c] = 0
for c in sys.argv[1]:
    dic[c] += 1
print("Char count:")
dic_o = sorted(dic.items())
for c in dic_o:
    print(c[0],"=",c[1])
import random

list = []

for x in range(1000):
    x = random.randint(0, 999)
    list.append(x)
print(list)

f = open('log.txt', 'w')

for x in list:
    print(x)
    f.write(str(x))
    f.write('\n')

f.flush()

# テキストファイルとの接続を切る
f.close()
#ここまで最初の課題 （書き込み）

#ここから次の課題（読み込み）
with open("log.txt", "r") as f:
    line = f.readline()

    print(list)

    for x in list:
        if(x % 2 == 0):
            print(str(x) + " is even")
        else:
            print(str(x) + " is odd")








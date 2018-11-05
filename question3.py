import random
from collections import Counter
import statistics as st

sum = 0
list = []

for i in range(1000):
    i = random.randint(1, 6)
    sum = sum + i
    list.append(i)

list.sort()
# N=1000
N = len(list)

print("合計は" + str(sum))


def average():  # 平均値を求める
    ave = sum / N
    print("平均は" + str(ave))


def median():  # 中央値を求める
    median1 = N / 2
    median2 = N / 2 + 1
    median1 = int(median1) - 1
    median2 = int(median2) - 1
    med = (list[median1] + list[median2]) / 2
    print("中央値は" + str(med))


def mode():  # 最頻値を求める
    c = Counter(list)
    mod = c.most_common(1)
    print("最頻値は" + str(mod[0][0]) + "で" + str(mod[0][1]) + "個ありました")


def sd():  # 標準偏差を求める
    print("標準偏差は" + str(st.stdev(list)))

average()
median()
mode()
sd()

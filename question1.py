import math

number = input("数字を入力してください")
number = int(number)

if(number<=0):
    print("入力された数字が0以下なので終了します")
    exit(1)

def trial_division(target):
    dest = int(math.sqrt(target))

    for i in range(2, dest):
        if target % i == 0:
            print(str(target) + 'は素数ではありません')
            return
    print(str(target) + 'は素数です')

trial_division(number)
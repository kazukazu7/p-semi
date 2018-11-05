number = input("0より大きい数字を入力してください")
str = number
number = int(number)

if(number <= 0):
    print("0より大きい数字を入力してください")
    exit(1)

def FizzBuzz():
    if(number % 15  == 0):
        print("FizzBuzz")
    elif(number % 5 == 0):
        print("fizz")
    elif(number % 3 == 0):
        print("buzz")
    else:
        print(str)

FizzBuzz()






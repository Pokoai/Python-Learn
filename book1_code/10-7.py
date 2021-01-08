print("输入两个数字，求之和")

while True:
    try:
        first_num = int(input("input first number: "))
        second_num = int(input("input second number: "))
    except ValueError:
        print("输入错误，请重新输入数字")
    else:
        print("sum = " + str(first_num + second_num))
    
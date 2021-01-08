active = True
filename = 'guest_book.txt'
while active:
    name = input("请输入你的名字；")
    print(name.title() + ", welcom to my site.")

    with open(filename, 'a') as file_object:
        file_object.write(name + "\n")
    
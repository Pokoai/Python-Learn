def show_magicians(magicians_list):
    print("有请以下魔术家登场：")
    for magician in magicians_list:
        print(magician)

def make_great(magicians_list, magicians_NewList):
    while magicians_list:
        magician = magicians_list.pop().title()
        magician = "the Great " + magician
        magicians_NewList.append(magician)
    

magicians = ['jk', 'dfdg', 'fddfh', '54hth', 'errtyy7']
magicians_NewList = []

make_great(magicians[:], magicians_NewList)
show_magicians(magicians_NewList)
show_magicians(magicians)
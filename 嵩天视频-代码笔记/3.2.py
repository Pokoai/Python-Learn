import random

def send_invit(name_list):
    for i in name_list:
        print(i.title() + ', ',  end="")
    print("你们可以和我一起共进晚餐吗？\n")

invit_persons = ['xiaobao', 'ruirui', 'dabao']
send_invit(invit_persons)

print("ruirui 无法赴约")
invit_persons[1] = 'chaochao'
send_invit(invit_persons)

print("我找到了一个更大的餐桌")
invit_persons.insert(0, 'hanhan')
invit_persons.insert(2, 'gaga')
invit_persons.append('zouzou')
send_invit(invit_persons)

print("抱歉，我只能邀请两位朋友了")
#print(invit_persons)
for i in range(4):
    pop_num = random.randint(0, len(invit_persons) - 2)
    print( "{}, 对不起，我不能邀请你了".format(invit_persons.pop(pop_num)))

print("\n%s, %s 你们仍然在邀请之列" % (invit_persons[0], invit_persons[1]) )

del invit_persons[0] 
del invit_persons[0] 
if(len(invit_persons) == 0):
    print("列表为空")


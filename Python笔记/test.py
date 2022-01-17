import threading, time

# 银行存款
balance = 0


# 存取函数
def change_it(n):
    # 先存后取，结果应该不变，为0
    global balance
    balance = balance + n
    balance = balance - n


# 执行数次
def run_thread(n):
    for i in range(2000000):
        change_it(n)


# 创建两个线程
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))

t1.start()
t2.start()

t1.join()
t2.join()

print(balance)
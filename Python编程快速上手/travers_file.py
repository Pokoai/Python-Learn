import os

for folderName, subfolders, filenames in os.walk("D:\\Media\\Desktop\\Doc"):
    # print("当前目录：" + folderName)
    #
    # for subfolder in subfolders:
    #     print("子文件夹：" + subfolder)

    # 遍历所有文件
    for filename in filenames:
        print("文件：" + filename)

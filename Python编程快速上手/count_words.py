def count_words(file_name):
    """计算一个文件中有多少单词"""
    try:
        with open(file_name, encoding='utf-8') as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + file_name + "does not exist."
    else:
        # 计算文件大致包含多少单词
        words = contents.split()
        num_words = len(words)
        print("The file " " has about " + str(num_words) + " words.")

file_path = "D:\\Media\\Desktop\\Alice’s Adventures in Wonderland.txt"
count_words(file_path)

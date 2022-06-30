#! python
# 多行文本添加无序列表标记

import pyperclip

# 将已经复制过的文本粘贴到 text 中
text = pyperclip.paste()

# 每行文本前面加上 ‘- ’
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '- ' + lines[i]

text = ''.join(lines)

# 处理好的文本拷贝到剪贴板中待用
pyperclip.copy(text)



import os

txt_files = []
for root, dirs, files in os.walk('.'):  # 遍历当前目录及子目录
    for file in files:
        if file.endswith('.txt'):
            txt_files.append(os.path.join(file))  # 包含完整路径

with open('Library_book_div.txt', 'w') as f:
    for txt_file in txt_files:
        file_name = "'"+txt_file+"'"
        file_name2 = txt_file.split('.')[0]
        # <div class="book-link" onclick="loadBook('book1.txt')">book1</div>
        print(f'<div class="book-link" onclick="loadLibraryBook({file_name})">{file_name2}</div>')
        f.write(f'<div class="book-link" onclick="loadLibraryBook({file_name})">{file_name2}</div>\n')



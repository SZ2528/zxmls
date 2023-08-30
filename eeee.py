import os
import re

def split_markdown_file(filename):
    # 创建目标文件夹
    output_folder = 'ooo'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    sections = content.split('<HR>\n')

    for section in sections:
        lines = section.strip().split('\n')
        if lines:
            title_line = lines[0].strip()
            match = re.search(r'(?<=\*\*)\w+', title_line)  # 使用正则表达式提取标题编号
            if match:
                title = match.group()
                
                # 输出当前文件的标题
                print('当前文件标题:', title_line)
                
                # 手动输入日期
                date = input('请输入日期(格式:YYYY-MM-DD):')
                if(date==""): continue
                
                # 构建文件名
                file_name = f'{output_folder}/{date}-{title}.md'
                
                # 替换标题行的格式
                new_title_line = '---\nlayout: mypost\ntitle: ' + title_line[title_line.find('-')+1:].strip() + '\ncategories: []\n---'
                lines[0] = new_title_line

                with open(file_name, 'w', encoding='utf-8') as output_file:
                    output_file.write('\n'.join(lines))

    print(f'Successfully split the markdown file into {len(sections)} sections.')

# 使用示例
split_markdown_file('README.md')

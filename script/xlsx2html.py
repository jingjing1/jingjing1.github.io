import pandas as pd

# 读取xlsx文件
file_path = '/home/ubuntu/jpk/Unsorted_Papers_fill.xlsx'  # 替换为你的xlsx文件路径
sheet_name = 0  # 如果有多个sheet，修改为对应sheet名或索引
df = pd.read_excel(file_path, sheet_name=sheet_name)

# 构建HTML <li> 格式字符串
html_list = ""
for _, row in df.iterrows():
    html_list += (
        f"<li> {row['Title']} &nbsp "
        f"<a href=\"{row['pdf_link']}\">[pdf]</a> &nbsp"
        f"<a href=\"{row['code_link']}\">[code]</a> <br>"
        f"{row['Authors']} <br>"
        f"{row['Publisher']} <br><br></li>\n"
    )

data = f"<ul>\n{html_list}</ul>"

data = data.replace('Jingjing Chen', '<b>Jingjing Chen</b>')
data = data.replace('<a href="nan">[pdf]</a> &nbsp', '')
data = data.replace('<a href="nan">[code]</a>', '')

# 保存HTML代码到文件
output_file = 'output.txt'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(data)

print("HTML代码已生成并保存到", output_file)



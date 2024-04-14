#遍历目录及子文件夹中的word文件
import os
import time
from tkinter import Tk
from tkinter.filedialog import askdirectory
from win32com.client import DispatchEx
from pdf2image import convert_from_path


def convert_pdf(pdf_path, save_directory="temp", resolution=400):
    pages = convert_from_path(pdf_path, resolution)
    save_name = pdf_path.split('\\')[-1].split('.')[0]

    for idx, page in enumerate(pages):
        page.save(f'{save_directory}/{save_name}_{idx+1}.png', 'PNG')

# 打开选择目录的对话框
Tk().withdraw()  # 隐藏Tkinter根窗口
word_dir = askdirectory(title="选择Word文件所在目录")

# 遍历目录中的Word文件
word_files = [f for f in os.listdir(word_dir) if not f.startswith("~") and f.endswith(".doc")]
word_files = [os.path.join(word_dir, f) for f in word_files]

# 创建Word应用程序对象
word_app = DispatchEx("Word.Application")

# 遍历Word文件进行转换
for word_file in word_files:
    print(f'转换中:{word_file}')

    # 转换为PDF并保存到Word所在目录
    pdf_file = os.path.splitext(word_file)[0] + ".pdf"
    #pdf_file = "temp.pdf"
    doc = word_app.Documents.Open(word_file)
    doc.SaveAs(pdf_file, FileFormat=17)
    doc.Close()
    print(f'已存檔:{pdf_file}')

    # 将PDF转换为图片
    convert_pdf(pdf_path=pdf_file)

    # 删除PDF文件
    os.remove(pdf_file)
    print(f"删除PDF文件:{pdf_file}")

# 关闭Word应用程序
word_app.Quit()

time.sleep(3)

print("轉存圖片完成!!")
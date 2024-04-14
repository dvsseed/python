#遍历目录及子文件夹中的word文件
import os
import glob
from win32com.client import DispatchEx
from pdf2image import convert_from_path


def convert_word_to_jpg(word_file):
    # 创建Word应用程序对象
    word_app = DispatchEx("Word.Application")
     
    # 遍历Word文件进行转换
    print(f'轉換中：{word_file}')
    
    # 转换为PDF并保存到Word所在目录
    pdf_file = os.path.splitext(word_file)[0] + ".pdf"
    doc = word_app.Documents.Open(word_file)
    doc.SaveAs(pdf_file, FileFormat=17)
    doc.Close()
    
    # 将PDF转换为图片
    images = convert_from_path(pdf_file)
 
    # 保存图片
    for i, image in enumerate(images):
        image_file = "temp/" + os.path.splitext(pdf_file)[0] + f"_page_{i + 1}.jpg"  # 设置图片文件名
        image.save(image_file, "JPEG")
        print(f"保存圖片：{image_file}")
 
    # 删除PDF文件
    # os.remove(pdf_file)
    # print(f"删除PDF文件：{pdf_file}")
     
    # 关闭Word应用程序
    word_app.Quit()


def main():
    # 創建 temp 子目錄
    temp_dir = "temp"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    # 遍歷當前目錄中的 Word 文件
    word_files = glob.glob("*.doc")  # + glob.glob("*.doc") + glob.glob("*.dotx")

    # 遍歷 Word 文件進行轉換
    for word_file in word_files:
        convert_word_to_jpg(word_file)

    print("轉換完成！")


if __name__ == "__main__":
    main()
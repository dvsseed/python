import cv2
import pytesseract
import re

# 设置 Tesseract 路径（根据你的安装路径修改）
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_image(image_path, start_from_line=1):
    # 读取图像
    img = cv2.imread(image_path)

    # 使用 pytesseract 进行 OCR
    text = pytesseract.image_to_string(img, lang='chi_tra')

    # 按行分割文本
    lines = text.split('\n')

    # 删除空白行和指定的起始行之前的行
    non_empty_lines = [line.strip() for line in lines if line.strip() and lines.index(line) >= start_from_line - 1]

    # 连接非空行并删除空格
    cleaned_text = '\n'.join(non_empty_lines).replace(' ', '')

    return cleaned_text

def save_text_to_file(text, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(text)

if __name__ == "__main__":
    input_image_path = '11300XX_1.png'  # 輸入圖像路徑
    output_file_path = 'output_text.txt'  # 輸出文本文件路徑
    starting_line = 11  # 開始辨識的行數

    text = ocr_image(input_image_path, start_from_line=starting_line)
    save_text_to_file(text, output_file_path)

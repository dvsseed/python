import pytesseract
from PIL import Image
import os

# 获取当前目录
current_directory = os.getcwd()

# 遍历当前目录下的所有文件
for filename in os.listdir(current_directory):
    if filename.endswith(".png"):
        img_fp = os.path.join(current_directory, filename)
        print(f'圖像辨識檔案:{img_fp}')
        
        # 进行文字识别
        text = pytesseract.image_to_string(Image.open(img_fp), lang='chi_tra')
        
        # 指定从第几行开始识别（例如从第10行开始）
        start_line = 11
        
        # 将结果保存到文件
        output_file = './output.txt'
        with open(output_file, 'w', encoding='utf-8') as f:  # 使用 'a' 模式以追加方式写入文件
            lines = text.split('\n')
            for i, line in enumerate(lines):
                line = line.strip()
                if line and i + 1 >= start_line:
                    f.write(line.replace(' ', '') + '\n')  # 删除空格

# 检查是否有输出
if os.path.getsize(output_file) == 0:
    print("識別結果為空，請檢查程式碼或輸入圖像。")
else:
    print(f"OCR 辨識結果已保存到 {output_file}")

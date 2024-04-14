import pytesseract
from PIL import Image
import os

# 你的圖片路徑
img_fp = './11300XX_1.png'

# 進行文字識別
text = pytesseract.image_to_string(Image.open(img_fp), lang='chi_tra')

# 指定從第幾行開始辨識（例如從第10行開始）
start_line = 11

# 將結果保存到文件
output_file = './output.txt'
with open(output_file, 'w', encoding='utf-8') as f:
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if line and i + 1 >= start_line:
            f.write(line.replace(' ', '') + '\n')  # 刪除空格

# 检查是否有输出
if os.path.getsize(output_file) == 0:
    print("識別結果為空，請檢查程式碼或輸入圖像。")
else:
    print(f"OCR 辨識結果已保存到 {output_file}")

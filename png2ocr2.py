import os
from cnocr import CnOcr

# 你的圖片路徑
img_fp = './11300XX_1.png'

# 創建 CnOcr 實例
ocr = CnOcr()

# 進行文字識別
out = ocr.ocr(img_fp)

# 指定從第幾行開始辨識（例如從第2行開始）
start_line = 1

# 將結果保存到文件
output_file = './output.txt'
with open(output_file, 'w', encoding='utf-8') as f:
    for i, line in enumerate(out):
        # 去除空白行
        if line and isinstance(line, list):
            line_text = ''.join(line)
            line_text = line_text.strip()  # 去除空白字符
            if line_text:  # 如果不是空行
                if i + 1 >= start_line:
                    f.write(line_text + '\n')

# 检查是否有输出
if os.path.getsize(output_file) == 0:
    print("識別結果為空，請檢查程式碼或輸入圖像。")
else:
    print(f"OCR 辨識結果已保存到 {output_file}")

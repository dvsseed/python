import opencc
import os

# 設置簡體中文到繁體中文的轉換器
converter = opencc.OpenCC('s2twp.json')  # s2twp.json包含簡體到繁體的轉換規則

# 輸入和輸出文件的路徑
input_file_path = '简体中文.txt'
output_file_path = '繁體中文.txt'

# 檢查輸入文件是否存在
if not os.path.exists(input_file_path):
    print("錯誤：找不到指定的简体中文文件。")
else:
    # 讀取簡體中文文件並轉換為繁體中文
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        simplified_chinese_text = input_file.read()
        traditional_chinese_text = converter.convert(simplified_chinese_text)

    # 寫入繁體中文文件
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(traditional_chinese_text)

    print("简体中文.txt已轉換為繁體中文，並保存為繁體中文.txt。")

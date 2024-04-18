import win32com.client
import datetime
import os

def modify_and_save_doc_file(file_path):
    # 创建 Word 应用程序对象
    word_app = win32com.client.Dispatch("Word.Application")

    # 打开文档
    doc = word_app.Documents.Open(file_path)

    # 替换文档中的文本
    for story_range in doc.StoryRanges:
        find_obj = story_range.Find
        find_obj.Text = "04月"
        find_obj.Replacement.Text = "05月"
        find_obj.Execute(Replace=2)

    # 获取当前月份
    current_month = datetime.datetime.now().month

    # 计算目标月份
    target_month = current_month + 1
    if target_month > 12:
        target_month -= 12  # 如果目标月份超过12，则取模回到1月

    # 构造新的文件名
    file_name_parts = os.path.splitext(os.path.basename(file_path))
    new_file_name = f"{file_name_parts[0][:-9]}{target_month:02d}月會報會議紀錄{file_name_parts[1]}"

    # 获取文件所在目录
    file_directory = os.path.dirname(file_path)

    # 保存修改后的 Word 文档
    new_file_path = os.path.join(file_directory, new_file_name)
    doc.SaveAs(new_file_path)

    # 关闭文档和 Word 应用程序
    doc.Close()
    word_app.Quit()

    print(f"文件已另存為：{new_file_path}")

# 要修改的 Word 文件路径
word_file_path = r"C:\Users\dvsse\(公文)宜蘭下水道精進維護_11300XX_檢送11304月會報會議紀錄.doc"
modify_and_save_doc_file(word_file_path)

import os
import shutil


def move_file_to_folder(filename):
    # 获取文件名（不带扩展名）和文件夹名
    basename = os.path.splitext(filename)[0]
    foldername = basename

    # 如果文件夹不存在，则创建文件夹
    if not os.path.exists(foldername):
        os.makedirs(foldername)

    # 移动文件到文件夹中
    try:
        shutil.move(filename, os.path.join(foldername, filename))
        print(f"文件 '{filename}' 已成功移动到文件夹 '{foldername}' 中。")
    except Exception as e:
        print(f"移动文件 '{filename}' 到文件夹 '{foldername}' 失败：{e}")


if __name__ == "__main__":
    filename = "(公文)112年度精進及維護_11303_檢送作業系統安全性及穩定性測試更新報告_V1.pdf"  # 要移动的文件名
    move_file_to_folder(filename)

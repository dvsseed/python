import os
import shutil


def move_pdfs_to_folders():
    # 获取当前目录下的所有文件
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    
    # 遍历文件
    for filename in files:
        # 检查文件是否为PDF文件
        if filename.lower().endswith('.pdf'):
            # 获取文件名（不带扩展名）
            basename = os.path.splitext(filename)[0]
            foldername = basename

            # 创建文件夹
            if not os.path.exists(foldername):
                os.makedirs(foldername)

            # 移动文件到文件夹中
            try:
                shutil.move(filename, os.path.join(foldername, filename))
                print(f"文件 '{filename}' 已成功移動到文件夾 '{foldername}' 中。")
            except Exception as e:
                print(f"移動文件 '{filename}' 到文件夾 '{foldername}' 失敗：{e}")


if __name__ == "__main__":
    move_pdfs_to_folders()

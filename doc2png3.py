from win32com.client import Dispatch
import pyautogui
import win32gui
import time
import os
import glob


def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))


def convert_word_to_jpg(word_file):
    shotfile = 'temp/shot.png'

    # word = win32.gencache.EnsureDispatch('Word.Application')
    word = Dispatch('Word.Application')
    word.Visible = True
    word.WindowState = 1  # maximize

    top_windows = []
    win32gui.EnumWindows(windowEnumerationHandler, top_windows)

    for i in top_windows:  # all open apps
        if "word" in i[1].lower():  # find word (assume only one)
            try:
                win32gui.ShowWindow(i[0],5)
                win32gui.SetForegroundWindow(i[0])  # bring to front
                break
            except:
                pass

    print(word_file)
    doc = word.Documents.Open(word_file)  # open file

    time.sleep(3)  # wait for doc to load

    myScreenshot = pyautogui.screenshot()  # take screenshot
    myScreenshot.save(shotfile)  # save screenshot

    # close doc and word app
    doc.Close()
    word.Application.Quit()


def main():
    # 創建 temp 子目錄
    temp_dir = "temp"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    # 遍歷當前目錄中的 Word 文件
    word_files = glob.glob("*.doc")  # + glob.glob("*.docx") + glob.glob("*.dotx")

    # 遍歷 Word 文件進行轉換
    for word_file in word_files:
        convert_word_to_jpg(word_file)

    print("轉換完成！")


if __name__ == "__main__":
    main()
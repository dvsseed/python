import pygetwindow as gw
import pyautogui
import time  # 添加时间模块


def find_chrome_window():
    # 查找所有具有 "Chrome" 字符串的窗口，通常这是Chrome浏览器的进程名
    chrome_windows = [window for window in gw.getAllWindows() if "Chrome" in window.title]
    # 如果找到了Chrome窗口，则返回第一个找到的窗口
    if chrome_windows:
        return chrome_windows[0]
    else:
        print("找不到Chrome視窗")
        return None

def get_active_window_title():
    active_window = gw.getActiveWindow()
    if active_window is not None:
        return active_window.title
    else:
        return None

# 根据窗口标题查找窗口
def find_window(title):
    try:
        return gw.getWindowsWithTitle(title)[0]
    except IndexError:
        print("找不到指定標題的視窗")
        return None

# 捕获窗口截图
def capture_window_screenshot(window):
    if window is not None:
        window.activate()
        time.sleep(1)  # 等待窗口激活
        screenshot = pyautogui.screenshot(region=(window.left, window.top, window.width, window.height))
        screenshot.save("window_screenshot.png")
        print("視窗擷圖已保存為 window_screenshot.png")


# 主程序
if __name__ == "__main__":
    '''
    window_title = r"Notepad++"  # 替换为您要捕获的窗口的标题
    window = find_window(window_title)
    capture_window_screenshot(window)
    '''
    chrome_window = find_chrome_window()
    capture_window_screenshot(chrome_window)

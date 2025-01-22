import pygetwindow as gw
import pyautogui
import time

# 获取 MuMu 模拟器窗口
window_title = "MuMu模拟器12"  # 这里替换为实际的窗口标题
window = gw.getWindowsWithTitle(window_title)

if window:
    # 获取窗口的左上角坐标和宽高
    window = window[0]
    window_left, window_top = window.topleft
    window_width, window_height = window.size
    
    # 按钮的坐标
    button_coords = [
        [900, 300],  # 奖励按钮坐标
        [200, 360],  # 立即前往按钮坐标
        [900, 65], #关闭以及活动按钮
        [460,524],[],
        [],
        [],
    ]

    #轻松模式（simple_style）:活跃度100即可
    screen_x,screen_y  = window_left + button_coords[3][0],window_top + button_coords[3][1]
    pyautogui.click(screen_x, screen_y)
    time.sleep(1) #点击奖励按钮

    # screen_x,screen_y  = window_left + button_coords[0][0],window_top + button_coords[0][1]
    # pyautogui.click(screen_x, screen_y)
    # time.sleep(1) #点击奖励按钮

    # screen_x,screen_y  = window_left + button_coords[1][0],window_top + button_coords[1][1]
    # pyautogui.click(screen_x, screen_y)
    # time.sleep(1) #点击立即前往按钮






else:
    print("未找到MuMu模拟器12")

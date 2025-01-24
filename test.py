import pyautogui
import cv2
import numpy as np
import time
import pygetwindow as gw

def click_third_button():
    # 获取模拟器窗口的左上角位置和大小
    window_title = "MuMu模拟器12"
    window = gw.getWindowsWithTitle(window_title)
    
    if not window:
        print("未找到窗口")
        return
    
    window = window[0]  
    window_left, window_top = window.topleft  
    window_width, window_height = window.size  

    # 截取窗口内的屏幕
    screenshot = pyautogui.screenshot(region=(window_left, window_top, window_width, window_height))
    screenshot_np = np.array(screenshot)  # 转换为 NumPy 数组
    screenshot_rgb = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)  # 转为 BGR 格式

    # 加载按钮模板图像（彩色）
    button_template = cv2.imread('button/gonow.png')  # 读取按钮模板（彩色）
    template_h, template_w, _ = button_template.shape  # 获取模板大小

    # 进行模板匹配
    result = cv2.matchTemplate(screenshot_rgb, button_template, cv2.TM_CCOEFF_NORMED)

    # 设置匹配的阈值
    threshold = 0.5
    locations = np.where(result >= threshold)

    # 获取所有匹配的位置并按 x 坐标排序
    points = sorted(zip(*locations[::-1]), key=lambda pt: pt[0])

    if len(points) < 3:
        print("未找到足够的按钮进行点击")
        return
    
    # 选择第3个按钮
    target_pt = points[2]  # 第3个匹配点
    print(f"第3个按钮位置: {target_pt}")
    
    # 计算屏幕坐标（加上窗口偏移）
    screen_x = target_pt[0] + window_left + template_w // 2
    screen_y = target_pt[1] + window_top + template_h // 2

    # 点击目标位置
    pyautogui.click(screen_x, screen_y)
    print(f"已点击第3个按钮: ({screen_x}, {screen_y})")

# 调用函数
click_third_button()

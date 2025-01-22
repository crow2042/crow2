import pyautogui
import pygetwindow as gw
import numpy as np
import cv2
import time

def jiequ():
    window_title = "MuMu模拟器12"  
    window = gw.getWindowsWithTitle(window_title)

    window = window[0] 
    window_left, window_top = window.topleft 
    window_width, window_height = window.size 

    screenshot = pyautogui.screenshot(region=(window_left, window_top, window_width, window_height))
    screenshot_np = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)  

    button_template = cv2.imread('button/jiequ.png', 0) 

    result = cv2.matchTemplate(screenshot_gray, button_template, cv2.TM_CCOEFF_NORMED)

    threshold = 0.5
    locations = np.where(result >= threshold)

    for pt in zip(*locations[::-1]): 
        print(f"按钮找到在: {pt}")
        screen_x = pt[0] + window_left + button_template.shape[1] // 2
        screen_y = pt[1] + window_top + button_template.shape[0]// 2
        
        pyautogui.click(screen_x, screen_y)
        time.sleep(1)  

        break
import pyautogui
import pygetwindow as gw
import numpy as np
import cv2
import time
import random




def renwujihui():#任务集会所（有点杂
    window_title = "MuMu模拟器12"  
    window = gw.getWindowsWithTitle(window_title)

    window = window[0]  
    window_left, window_top = window.topleft  
    window_width, window_height = window.size  

    screenshot = pyautogui.screenshot(region=(window_left, window_top, window_width, window_height))
    screenshot_np = np.array(screenshot)  
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY) 

    button_template = cv2.imread('button/renwujihui.png', 0)  

    result = cv2.matchTemplate(screenshot_gray, button_template, cv2.TM_CCOEFF_NORMED)

    threshold = 0.8
    locations = np.where(result >= threshold)

    for pt in zip(*locations[::-1]):  
        print(f"按钮找到在: {pt}")
        screen_x = pt[0] + window_left + button_template.shape[1] // 2
        screen_y = pt[1] + window_top + button_template.shape[0] // 2
    
        pyautogui.click(screen_x, screen_y)
        time.sleep(1) 
        
        break

def quit():#退出（红叉叉
    window_title = "MuMu模拟器12"  
    window = gw.getWindowsWithTitle(window_title)

    window = window[0]  
    window_left, window_top = window.topleft  
    window_width, window_height = window.size  

    screenshot = pyautogui.screenshot(region=(window_left, window_top, window_width, window_height))
    screenshot_np = np.array(screenshot)  
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY) 

    button_template = cv2.imread('button/quit.png', 0)  

    result = cv2.matchTemplate(screenshot_gray, button_template, cv2.TM_CCOEFF_NORMED)

    threshold = 0.5
    locations = np.where(result >= threshold)

    for pt in zip(*locations[::-1]):  
        print(f"按钮找到在: {pt}")
        screen_x = pt[0] + window_left + button_template.shape[1] // 2
        screen_y = pt[1] + window_top + button_template.shape[0] // 2
    
        pyautogui.click(screen_x, screen_y)
        time.sleep(1) 

        break

def reward_1():#奖励
    window_title = "MuMu模拟器12"  
    window = gw.getWindowsWithTitle(window_title)

    window = window[0]  
    window_left, window_top = window.topleft  
    window_width, window_height = window.size  

    screenshot = pyautogui.screenshot(region=(window_left, window_top, window_width, window_height))
    screenshot_np = np.array(screenshot)  
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY) 

    button_template = cv2.imread('button/reward.png', 0)  

    result = cv2.matchTemplate(screenshot_gray, button_template, cv2.TM_CCOEFF_NORMED)

    threshold = 0.5
    locations = np.where(result >= threshold)

    for pt in zip(*locations[::-1]):  
        print(f"按钮找到在: {pt}")
        screen_x = pt[0] + window_left + button_template.shape[1] // 2
        screen_y = pt[1] + window_top + button_template.shape[0] // 2
    
        pyautogui.click(screen_x, screen_y)
        time.sleep(1) 

        break 

def gonow_1():#点第一个立即前往
    window_title = "MuMu模拟器12"  
    window = gw.getWindowsWithTitle(window_title)

    window = window[0]  
    window_left, window_top = window.topleft  
    window_width, window_height = window.size  

    screenshot = pyautogui.screenshot(region=(window_left, window_top, window_width, window_height))
    screenshot_np = np.array(screenshot)  
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY) 

    button_template = cv2.imread('button/gonow.png', 0)  

    result = cv2.matchTemplate(screenshot_gray, button_template, cv2.TM_CCOEFF_NORMED)

    threshold = 0.5
    locations = np.where(result >= threshold)

    for pt in zip(*locations[::-1]):  
        print(f"按钮找到在: {pt}")
        screen_x = pt[0] + window_left + button_template.shape[1] // 2
        screen_y = pt[1] + window_top + button_template.shape[0] // 2
    
        pyautogui.click(screen_x, screen_y)
        time.sleep(1) 

        break

def gonow_2():#点第二个立即前往
    window_title = "MuMu模拟器12"  
    window = gw.getWindowsWithTitle(window_title)

    window = window[0]  
    window_left, window_top = window.topleft  
    window_width, window_height = window.size  

    screenshot = pyautogui.screenshot(region=(window_left, window_top, window_width, window_height))
    screenshot_np = np.array(screenshot)  
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY) 

    button_template = cv2.imread('button/gonow.png', 0)  

    result = cv2.matchTemplate(screenshot_gray, button_template, cv2.TM_CCOEFF_NORMED)

    threshold = 0.5
    locations = np.where(result >= threshold)

    for pt in zip(*locations[::-1]):  
        print(f"按钮找到在: {pt}")
        screen_x = pt[1] + window_left + button_template.shape[1] // 2
        screen_y = pt[1] + window_top + button_template.shape[0] // 2
    
        pyautogui.click(screen_x, screen_y)
        time.sleep(1) 

        break    

def gonow_3():#点第三个立即前往
    window_title = "MuMu模拟器12"  
    window = gw.getWindowsWithTitle(window_title)

    window = window[0]  
    window_left, window_top = window.topleft  
    window_width, window_height = window.size  

    screenshot = pyautogui.screenshot(region=(window_left, window_top, window_width, window_height))
    screenshot_np = np.array(screenshot)  
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY) 

    button_template = cv2.imread('button/gonow.png', 0)  

    result = cv2.matchTemplate(screenshot_gray, button_template, cv2.TM_CCOEFF_NORMED)

    threshold = 0.5
    locations = np.where(result >= threshold)

    for pt in zip(*locations[::-1]):  
        print(f"按钮找到在: {pt}")

        screen_x_1 = pt[0] + window_left + button_template.shape[1] // 2
        screen_y_1= pt[1] + window_top + button_template.shape[0] // 2
        screen_x = pt[1] + window_left + button_template.shape[1] // 2
        screen_y = pt[1] + window_top + button_template.shape[0] // 2

       
        
        print(screen_x,screen_y)

        print(screen_x_1,screen_y_1)

        screen_x_2 = screen_x - screen_x_1 + screen_x
        pyautogui.click(screen_x_2, screen_y)
        time.sleep(1) 

        break    

def if_click():#判断屏幕上是否有退出按钮（没用上
    while True:

        window_title = "MuMu模拟器12"  
        window = gw.getWindowsWithTitle(window_title)

        window = window[0]  
        window_left, window_top = window.topleft  
        window_width, window_height = window.size  


        screenshot = pyautogui.screenshot(region=(window_left, window_top, window_width, window_height))
        screenshot_np = np.array(screenshot)  
        screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY) 


        button_template = cv2.imread('button/quit.png', 0)  


        result = cv2.matchTemplate(screenshot_gray, button_template, cv2.TM_CCOEFF_NORMED)


        threshold = 0.55
        locations = np.where(result >= threshold)

    
        for pt in zip(*locations[::-1]):  
            print(f"按钮找到在: {pt}")

            screen_x = pt[0] + window_left + button_template.shape[1] // 2
            screen_y = pt[1] + window_top + button_template.shape[0] // 2
            
            time.sleep(1)

            pyautogui.click(screen_x, screen_y)
            time.sleep(1) 
            
            return True

def jyfb():#精英副本
    window_title = "MuMu模拟器12"  
    window = gw.getWindowsWithTitle(window_title)

    window = window[0] 
    window_left, window_top = window.topleft 
    window_width, window_height = window.size 

    screenshot = pyautogui.screenshot(region=(window_left, window_top, window_width, window_height))
    screenshot_np = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)  

    button_template = cv2.imread('button/jyfb.png', 0) 

    result = cv2.matchTemplate(screenshot_gray, button_template, cv2.TM_CCOEFF_NORMED)

    threshold = 0.8
    locations = np.where(result >= threshold)

    for pt in zip(*locations[::-1]): 
        print(f"按钮找到在: {pt}")
        screen_x = pt[0] + window_left + button_template.shape[1] // 2
        screen_y = pt[1] + window_top + button_template.shape[0] // 2
        
        pyautogui.click(screen_x, screen_y)
        time.sleep(1)  

        break

def bjsd():#便捷扫荡
    window_title = "MuMu模拟器12"  
    window = gw.getWindowsWithTitle(window_title)

    window = window[0] 
    window_left, window_top = window.topleft 
    window_width, window_height = window.size 

    screenshot = pyautogui.screenshot(region=(window_left, window_top, window_width, window_height))
    screenshot_np = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)  

    button_template = cv2.imread('button/bjsd.png', 0) 

    result = cv2.matchTemplate(screenshot_gray, button_template, cv2.TM_CCOEFF_NORMED)

    threshold = 0.8
    locations = np.where(result >= threshold)

    for pt in zip(*locations[::-1]): 
        print(f"按钮找到在: {pt}")
        screen_x = pt[0] + window_left + button_template.shape[1] // 2
        screen_y = pt[1] + window_top + button_template.shape[0] // 2
        
        pyautogui.click(screen_x, screen_y)
        time.sleep(1)  

        break

def quanxuan():#一键全选
    window_title = "MuMu模拟器12"  
    window = gw.getWindowsWithTitle(window_title)

    window = window[0] 
    window_left, window_top = window.topleft 
    window_width, window_height = window.size 

    screenshot = pyautogui.screenshot(region=(window_left, window_top, window_width, window_height))
    screenshot_np = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)  

    button_template = cv2.imread('button/quanxuan.png', 0) 

    result = cv2.matchTemplate(screenshot_gray, button_template, cv2.TM_CCOEFF_NORMED)

    threshold = 0.8
    locations = np.where(result >= threshold)

    for pt in zip(*locations[::-1]): 
        print(f"按钮找到在: {pt}")
        screen_x = pt[0] + window_left + button_template.shape[1] // 2
        screen_y = pt[1] + window_top + button_template.shape[0] // 2
        
        pyautogui.click(screen_x, screen_y)
        time.sleep(1)  

        break

def saodang():#扫荡
    window_title = "MuMu模拟器12"  
    window = gw.getWindowsWithTitle(window_title)

    window = window[0] 
    window_left, window_top = window.topleft 
    window_width, window_height = window.size 

    screenshot = pyautogui.screenshot(region=(window_left, window_top, window_width, window_height))
    screenshot_np = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)  

    button_template = cv2.imread('button/saodang.png', 0) 

    result = cv2.matchTemplate(screenshot_gray, button_template, cv2.TM_CCOEFF_NORMED)

    threshold = 0.8
    locations = np.where(result >= threshold)

    for pt in zip(*locations[::-1]): 
        print(f"按钮找到在: {pt}")
        screen_x = pt[0] + window_left + button_template.shape[1] // 2
        screen_y = pt[1] + window_top + button_template.shape[0] // 2
        
        pyautogui.click(screen_x, screen_y)
        time.sleep(1)  

        break

def queding():#点击确定
    window_title = "MuMu模拟器12"  
    window = gw.getWindowsWithTitle(window_title)

    window = window[0] 
    window_left, window_top = window.topleft 
    window_width, window_height = window.size 

    screenshot = pyautogui.screenshot(region=(window_left, window_top, window_width, window_height))
    screenshot_np = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)  

    button_template = cv2.imread('button/queding.png', 0) 

    result = cv2.matchTemplate(screenshot_gray, button_template, cv2.TM_CCOEFF_NORMED)

    threshold = 0.8
    locations = np.where(result >= threshold)

    for pt in zip(*locations[::-1]): 
        print(f"按钮找到在: {pt}")
        screen_x = pt[0] + window_left + button_template.shape[1] // 2
        screen_y = pt[1] + window_top + button_template.shape[0] // 2
        
        pyautogui.click(screen_x, screen_y)
        time.sleep(1)  

        break

def qifu():#铜币祈福
    window_title = "MuMu模拟器12"  
    window = gw.getWindowsWithTitle(window_title)

    window = window[0] 
    window_left, window_top = window.topleft 
    window_width, window_height = window.size 

    screenshot = pyautogui.screenshot(region=(window_left, window_top, window_width, window_height))
    screenshot_np = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)  

    button_template = cv2.imread('button/qifu.png', 0) 

    result = cv2.matchTemplate(screenshot_gray, button_template, cv2.TM_CCOEFF_NORMED)

    threshold = 0.8
    locations = np.where(result >= threshold)

    for pt in zip(*locations[::-1]): 
        print(f"按钮找到在: {pt}")
        screen_x = pt[0] + window_left + button_template.shape[1] // 2
        screen_y = pt[1] + window_top + button_template.shape[0] // 2
        
        pyautogui.click(screen_x, screen_y)
        time.sleep(1)  

        break

def mfzc():#免费招财（两次
    window_title = "MuMu模拟器12"  
    window = gw.getWindowsWithTitle(window_title)

    window = window[0] 
    window_left, window_top = window.topleft 
    window_width, window_height = window.size 

    screenshot = pyautogui.screenshot(region=(window_left, window_top, window_width, window_height))
    screenshot_np = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)  

    button_template = cv2.imread('button/mfzc.png', 0) 

    result = cv2.matchTemplate(screenshot_gray, button_template, cv2.TM_CCOEFF_NORMED)

    threshold = 0.8
    locations = np.where(result >= threshold)

    for pt in zip(*locations[::-1]): 
        print(f"按钮找到在: {pt}")
        screen_x = pt[0] + window_left + button_template.shape[1] // 2
        screen_y = pt[1] + window_top + button_template.shape[0] // 2
        
        pyautogui.click(screen_x, screen_y)
        time.sleep(1)  

        break

def rzzm():#点击忍者招募
    window_title = "MuMu模拟器12"  
    window = gw.getWindowsWithTitle(window_title)

    window = window[0] 
    window_left, window_top = window.topleft 
    window_width, window_height = window.size 

    screenshot = pyautogui.screenshot(region=(window_left, window_top, window_width, window_height))
    screenshot_np = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)  

    button_template = cv2.imread('button/rzzm.png', 0) 

    result = cv2.matchTemplate(screenshot_gray, button_template, cv2.TM_CCOEFF_NORMED)

    threshold = 0.8
    locations = np.where(result >= threshold)

    for pt in zip(*locations[::-1]): 
        print(f"按钮找到在: {pt}")
        screen_x = pt[0] + window_left + button_template.shape[1] // 2
        screen_y = pt[1] + window_top + button_template.shape[0] // 2
        
        pyautogui.click(screen_x, screen_y)
        time.sleep(1)  

        break

def ptzm():#点击普通招募
    window_title = "MuMu模拟器12"  
    window = gw.getWindowsWithTitle(window_title)

    window = window[0] 
    window_left, window_top = window.topleft 
    window_width, window_height = window.size 

    screenshot = pyautogui.screenshot(region=(window_left, window_top, window_width, window_height))
    screenshot_np = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)  

    button_template = cv2.imread('button/ptzm.png', 0) 

    result = cv2.matchTemplate(screenshot_gray, button_template, cv2.TM_CCOEFF_NORMED)

    threshold = 0.6
    locations = np.where(result >= threshold)

    for pt in zip(*locations[::-1]): 
        print(f"按钮找到在: {pt}")
        screen_x = pt[0] + window_left + button_template.shape[1] // 2
        screen_y = pt[1] + window_top + button_template.shape[0] // 2
        
        pyautogui.click(screen_x, screen_y)
        time.sleep(1)  

        break

def mf():#点击免费x次
    window_title = "MuMu模拟器12"  
    window = gw.getWindowsWithTitle(window_title)

    window = window[0] 
    window_left, window_top = window.topleft 
    window_width, window_height = window.size 

    screenshot = pyautogui.screenshot(region=(window_left, window_top, window_width, window_height))
    screenshot_np = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)  

    button_template = cv2.imread('button/mf.png', 0) 

    result = cv2.matchTemplate(screenshot_gray, button_template, cv2.TM_CCOEFF_NORMED)

    threshold = 0.5
    locations = np.where(result >= threshold)

    for pt in zip(*locations[::-1]): 
        print(f"按钮找到在: {pt}")
        screen_x = pt[0] + window_left + button_template.shape[1] // 2
        screen_y = pt[1] + window_top + button_template.shape[0] // 2
        
        pyautogui.click(screen_x, screen_y)
        time.sleep(1)  

        break

def xiaoduituxi():#小队突袭
    window_title = "MuMu模拟器12"  
    window = gw.getWindowsWithTitle(window_title)

    window = window[0] 
    window_left, window_top = window.topleft 
    window_width, window_height = window.size 

    screenshot = pyautogui.screenshot(region=(window_left, window_top, window_width, window_height))
    screenshot_np = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)  

    button_template = cv2.imread('button/xiaoduituxi.png', 0) 

    result = cv2.matchTemplate(screenshot_gray, button_template, cv2.TM_CCOEFF_NORMED)

    threshold = 0.5
    locations = np.where(result >= threshold)

    for pt in zip(*locations[::-1]): 
        print(f"按钮找到在: {pt}")
        screen_x = pt[0] + window_left + button_template.shape[1] // 2
        screen_y = pt[1] + window_top + button_template.shape[0] // 2
        
        pyautogui.click(screen_x, screen_y)
        time.sleep(1)  

        break

def zuzhizhuzhan():#组织助战
    window_title = "MuMu模拟器12"  
    window = gw.getWindowsWithTitle(window_title)

    window = window[0] 
    window_left, window_top = window.topleft 
    window_width, window_height = window.size 

    screenshot = pyautogui.screenshot(region=(window_left, window_top, window_width, window_height))
    screenshot_np = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)  

    button_template = cv2.imread('button/zuzhizhuzhan.png', 0) 

    result = cv2.matchTemplate(screenshot_gray, button_template, cv2.TM_CCOEFF_NORMED)

    threshold = 0.5
    locations = np.where(result >= threshold)

    for pt in zip(*locations[::-1]): 
        print(f"按钮找到在: {pt}")
        screen_x = pt[0] + window_left + button_template.shape[1] // 2
        screen_y = pt[1] + window_top + button_template.shape[0] // 2
        
        pyautogui.click(screen_x, screen_y)
        time.sleep(1)  

        break

def wdzhuzhan():#我的助战
    window_title = "MuMu模拟器12"  
    window = gw.getWindowsWithTitle(window_title)

    window = window[0] 
    window_left, window_top = window.topleft 
    window_width, window_height = window.size 

    screenshot = pyautogui.screenshot(region=(window_left, window_top, window_width, window_height))
    screenshot_np = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)  

    button_template = cv2.imread('button/wdzhuzhan.png', 0) 

    result = cv2.matchTemplate(screenshot_gray, button_template, cv2.TM_CCOEFF_NORMED)

    threshold = 0.5
    locations = np.where(result >= threshold)

    for pt in zip(*locations[::-1]): 
        print(f"按钮找到在: {pt}")
        screen_x = pt[0] + window_left + button_template.shape[1] // 2
        screen_y = pt[1] + window_top + button_template.shape[0] // 2
        
        pyautogui.click(screen_x, screen_y)
        time.sleep(1)  

        break

def xdtx_lingqu():#领取小队突袭奖励
    window_title = "MuMu模拟器12"  
    window = gw.getWindowsWithTitle(window_title)

    window = window[0] 
    window_left, window_top = window.topleft 
    window_width, window_height = window.size 

    screenshot = pyautogui.screenshot(region=(window_left, window_top, window_width, window_height))
    screenshot_np = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)  

    button_template = cv2.imread('button/xdtx_lingqu.png', 0) 

    result = cv2.matchTemplate(screenshot_gray, button_template, cv2.TM_CCOEFF_NORMED)

    threshold = 0.5
    locations = np.where(result >= threshold)

    for pt in zip(*locations[::-1]): 
        print(f"按钮找到在: {pt}")
        screen_x = pt[0] + window_left + button_template.shape[1] // 2
        screen_y = pt[1] + window_top + button_template.shape[0] // 2
        
        pyautogui.click(screen_x, screen_y)
        time.sleep(1)  

        break

def yaoqing():#邀请
    window_title = "MuMu模拟器12"  
    window = gw.getWindowsWithTitle(window_title)

    window = window[0] 
    window_left, window_top = window.topleft 
    window_width, window_height = window.size 

    screenshot = pyautogui.screenshot(region=(window_left, window_top, window_width, window_height))
    screenshot_np = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)  

    button_template = cv2.imread('button/yaoqing.png', 0) 

    result = cv2.matchTemplate(screenshot_gray, button_template, cv2.TM_CCOEFF_NORMED)

    threshold = 0.5
    locations = np.where(result >= threshold)

    for pt in zip(*locations[::-1]): 
        print(f"按钮找到在: {pt}")
        screen_x = pt[0] + window_left + button_template.shape[1] // 2
        screen_y = pt[1] + window_top + button_template.shape[0] // 2
        
        pyautogui.click(screen_x, screen_y)
        time.sleep(1)  

        break

def chuzhan():#出战
    window_title = "MuMu模拟器12"  
    window = gw.getWindowsWithTitle(window_title)

    window = window[0] 
    window_left, window_top = window.topleft 
    window_width, window_height = window.size 

    screenshot = pyautogui.screenshot(region=(window_left, window_top, window_width, window_height))
    screenshot_np = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)  

    button_template = cv2.imread('button/chuzhan.png', 0) 

    result = cv2.matchTemplate(screenshot_gray, button_template, cv2.TM_CCOEFF_NORMED)

    threshold = 0.5
    locations = np.where(result >= threshold)

    for pt in zip(*locations[::-1]): 
        print(f"按钮找到在: {pt}")
        screen_x = pt[0] + window_left + button_template.shape[1] // 2
        screen_y = pt[1] + window_top + button_template.shape[0] // 2
        
        pyautogui.click(screen_x, screen_y)
        time.sleep(1)  

        break

def frzj():#丰饶之间
    window_title = "MuMu模拟器12"  
    window = gw.getWindowsWithTitle(window_title)

    window = window[0] 
    window_left, window_top = window.topleft 
    window_width, window_height = window.size 

    screenshot = pyautogui.screenshot(region=(window_left, window_top, window_width, window_height))
    screenshot_np = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)  

    button_template = cv2.imread('button/frzj.png', 0) 

    result = cv2.matchTemplate(screenshot_gray, button_template, cv2.TM_CCOEFF_NORMED)

    threshold = 0.5
    locations = np.where(result >= threshold)

    for pt in zip(*locations[::-1]): 
        print(f"按钮找到在: {pt}")
        screen_x = pt[0] + window_left + button_template.shape[1] // 2
        screen_y = pt[1] + window_top + button_template.shape[0] // 2
        
        pyautogui.click(screen_x, screen_y)
        time.sleep(1)  

        break

def tiaozhan():#tiaozhan
    window_title = "MuMu模拟器12"  
    window = gw.getWindowsWithTitle(window_title)

    window = window[0] 
    window_left, window_top = window.topleft 
    window_width, window_height = window.size 

    screenshot = pyautogui.screenshot(region=(window_left, window_top, window_width, window_height))
    screenshot_np = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)  

    button_template = cv2.imread('button/tiaozhan.png', 0) 

    result = cv2.matchTemplate(screenshot_gray, button_template, cv2.TM_CCOEFF_NORMED)

    threshold = 0.5
    locations = np.where(result >= threshold)

    for pt in zip(*locations[::-1]): 
        print(f"按钮找到在: {pt}")
        screen_x = pt[0] + window_left + button_template.shape[1] // 2
        screen_y = pt[1] + window_top + button_template.shape[0] // 2
        
        pyautogui.click(screen_x, screen_y)
        time.sleep(1)  

        break

def ptgj():#普通攻击
    window_title = "MuMu模拟器12"  
    window = gw.getWindowsWithTitle(window_title)

    window = window[0] 
    window_left, window_top = window.topleft 
    window_width, window_height = window.size 

    screenshot = pyautogui.screenshot(region=(window_left, window_top, window_width, window_height))
    screenshot_np = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)  

    button_template = cv2.imread('button/ptgj.png', 0) 

    result = cv2.matchTemplate(screenshot_gray, button_template, cv2.TM_CCOEFF_NORMED)

    threshold = 0.8
    locations = np.where(result >= threshold)

    for pt in zip(*locations[::-1]): 
        print(f"按钮找到在: {pt}")
        screen_x = pt[0] + window_left + button_template.shape[1] // 2
        screen_y = pt[1] + window_top + button_template.shape[0] // 2
        
        pyautogui.mouseDown(screen_x, screen_y)
        time.sleep(30)
        pyautogui.mouseUp(screen_x, screen_y)


        break

def random_click_in_window():#通过点击空白处场景
 
    window_title = "MuMu模拟器12"  
    window = gw.getWindowsWithTitle(window_title)
    window = window[0]  

    window_left, window_top = window.topleft
    window_width, window_height = window.size

    # 开始随机点击
    for _ in range(1):
        # 在窗口范围内随机生成点击坐标
        random_x = random.randint(window_left + 10, window_left + window_width - 10)
        random_y = random.randint(window_top + 10, window_top + window_height - 10)

        print(f"随机点击位置: ({random_x}, {random_y})")
        pyautogui.click(random_x, random_y)  # 执行点击操作
        time.sleep(0.5)  # 等待指定时间

def shilian():#试炼之地
    window_title = "MuMu模拟器12"  
    window = gw.getWindowsWithTitle(window_title)

    window = window[0] 
    window_left, window_top = window.topleft 
    window_width, window_height = window.size 

    screenshot = pyautogui.screenshot(region=(window_left, window_top, window_width, window_height))
    screenshot_np = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)  

    button_template = cv2.imread('button/shilian.png', 0) 

    result = cv2.matchTemplate(screenshot_gray, button_template, cv2.TM_CCOEFF_NORMED)

    threshold = 0.5
    locations = np.where(result >= threshold)

    for pt in zip(*locations[::-1]): 
        print(f"按钮找到在: {pt}")
        screen_x = pt[0] + window_left + button_template.shape[1] // 2
        screen_y = pt[1] + window_top + button_template.shape[0] // 2
        
        pyautogui.click(screen_x, screen_y)
        time.sleep(1)  

        break

def shengcuntiaozhan():#生存试炼
    window_title = "MuMu模拟器12"  
    window = gw.getWindowsWithTitle(window_title)

    window = window[0] 
    window_left, window_top = window.topleft 
    window_width, window_height = window.size 

    screenshot = pyautogui.screenshot(region=(window_left, window_top, window_width, window_height))
    screenshot_np = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)  

    button_template = cv2.imread('button/shengcuntiaozhan.png', 0) 

    result = cv2.matchTemplate(screenshot_gray, button_template, cv2.TM_CCOEFF_NORMED)

    threshold = 0.5
    locations = np.where(result >= threshold)

    for pt in zip(*locations[::-1]): 
        print(f"按钮找到在: {pt}")
        screen_x = pt[0] + window_left + button_template.shape[1] // 2
        screen_y = pt[1] + window_top + button_template.shape[0] // 2
        
        pyautogui.click(screen_x, screen_y)
        time.sleep(1)  

        break

def chongzhi():#重置生存试炼（后面接确定
    window_title = "MuMu模拟器12"  
    window = gw.getWindowsWithTitle(window_title)

    window = window[0] 
    window_left, window_top = window.topleft 
    window_width, window_height = window.size 

    screenshot = pyautogui.screenshot(region=(window_left, window_top, window_width, window_height))
    screenshot_np = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)  

    button_template = cv2.imread('button/chongzhi.png', 0) 

    result = cv2.matchTemplate(screenshot_gray, button_template, cv2.TM_CCOEFF_NORMED)

    threshold = 0.8
    locations = np.where(result >= threshold)

    for pt in zip(*locations[::-1]): 
        print(f"按钮找到在: {pt}")
        screen_x = pt[0] + window_left + button_template.shape[1] // 2
        screen_y = pt[1] + window_top + button_template.shape[0] // 2
        
        pyautogui.click(screen_x, screen_y)
        time.sleep(1)  

        break

def kaishisaodang():#重置生存试炼（后面接确定
    window_title = "MuMu模拟器12"  
    window = gw.getWindowsWithTitle(window_title)

    window = window[0] 
    window_left, window_top = window.topleft 
    window_width, window_height = window.size 

    screenshot = pyautogui.screenshot(region=(window_left, window_top, window_width, window_height))
    screenshot_np = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)  

    button_template = cv2.imread('button/kaishisaodang.png', 0) 

    result = cv2.matchTemplate(screenshot_gray, button_template, cv2.TM_CCOEFF_NORMED)

    threshold = 0.8
    locations = np.where(result >= threshold)

    for pt in zip(*locations[::-1]): 
        print(f"按钮找到在: {pt}")
        screen_x = pt[0] + window_left + button_template.shape[1] // 2
        screen_y = pt[1] + window_top + button_template.shape[0] // 2
        
        pyautogui.click(screen_x, screen_y)
        time.sleep(1)  

        break

def zhunbeijiuxu():#准备就绪
    window_title = "MuMu模拟器12"  
    window = gw.getWindowsWithTitle(window_title)

    window = window[0] 
    window_left, window_top = window.topleft 
    window_width, window_height = window.size 

    screenshot = pyautogui.screenshot(region=(window_left, window_top, window_width, window_height))
    screenshot_np = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)  

    button_template = cv2.imread('button/zhunbeijiuxu.png', 0) 

    result = cv2.matchTemplate(screenshot_gray, button_template, cv2.TM_CCOEFF_NORMED)

    threshold = 0.9
    locations = np.where(result >= threshold)

    for pt in zip(*locations[::-1]): 
        print(f"按钮找到在: {pt}")
        screen_x = pt[0] + window_left + button_template.shape[1] // 2
        screen_y = pt[1] + window_top + button_template.shape[0] // 2
        
        pyautogui.click(screen_x, screen_y)
        time.sleep(1)  

        break



def ez_model():  #简单模式
    #精英副本扫荡
    reward_1()
    time.sleep(3)
    gonow_1()
    time.sleep(3)
    jyfb()
    time.sleep(3)
    bjsd()
    time.sleep(3)
    quanxuan()
    time.sleep(3)
    saodang()
    time.sleep(5)
    quit()
    time.sleep(3)
    quit()
    time.sleep(3)
    quit()
    time.sleep(3)
    quit()
    time.sleep(3)
    quit()
    time.sleep(3)
    #组织祈福
    reward_1()
    time.sleep(3)
    gonow_1()
    time.sleep(5)
    qifu()
    time.sleep(5)
    quit()
    time.sleep(5)
    quit()
    time.sleep(3)
    quit()
    time.sleep(3)
    #铜币招财
    reward_1()
    time.sleep(3)
    gonow_1()
    time.sleep(3)
    mfzc()
    time.sleep(3)
    mfzc()
    time.sleep(3)
    quit()
    time.sleep(3)
    #忍者招募
    rzzm()
    time.sleep(3)
    ptzm()
    time.sleep(3)
    mf()
    time.sleep(3)
    queding()
    time.sleep(3)
    quit()
    time.sleep(3)
    #小队突袭
    xiaoduituxi()
    time.sleep(3)
    zuzhizhuzhan()
    time.sleep(3)
    yaoqing()
    time.sleep(3)
    chuzhan()
    time.sleep(60)
    zuzhizhuzhan()
    time.sleep(3)
    yaoqing()
    time.sleep(3)
    chuzhan()
    time.sleep(60)
    quit()
    time.sleep(3)
    #生存试炼
    shilian()
    time.sleep(3)
    shengcuntiaozhan()
    time.sleep(3)
    chongzhi()
    time.sleep(3)
    queding()
    time.sleep(3)
    kaishisaodang()
    time.sleep(3)
    zhunbeijiuxu()
    time.sleep(60)#不确定，后面要修改或者找一个检索方式
    quit()
    time.sleep(3)
    frzj()
    time.sleep(3)
    tiaozhan()
    time.sleep(3)
    ptgj()
    time.sleep(40)
    random_click_in_window()
    time.sleep(3)
    quit()







    return 0

gonow_3()



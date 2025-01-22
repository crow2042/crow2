import pyautogui
import pygetwindow as gw
import numpy as np
import cv2
import time




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

    threshold = 0.3
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

    threshold = 0.5
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



def ez_model():  #简单模式
    reward_1()
    gonow_1()
    jyfb()
    bjsd()
    quanxuan()
    saodang()
    time.sleep(5)
    quit()
    quit()
    quit()
    quit()
    quit()
    reward_1()
    gonow_1()
    qifu()
    time.sleep(3)
    quit()
    quit()
    quit()
    reward_1()
    gonow_1()
    mfzc()
    mfzc()
    quit()
    rzzm()
    ptzm()
    mf()
    time.sleep(1)
    queding()
    quit()
    xiaoduituxi()
    zuzhizhuzhan()
    time.sleep(1)
    yaoqing()
    chuzhan()

    return 0





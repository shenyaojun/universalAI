import pyautogui  
import time  
import random  
  


while True:

    # 移动鼠标到指定位置  
    random_number = random.randint(5, 100)  
    x, y = 800, 600  # 替换为你想要的位置坐标  
    pyautogui.moveTo(x, y+random_number)  
    
    # 执行鼠标左键点击操作  
    pyautogui.click()

    # 模拟鼠标中间键向上滚动  
    pyautogui.scroll(200)  
    
    # 模拟鼠标中间键向下滚动  
    pyautogui.scroll(-200)

    

    time.sleep(random_number)  # 休眠120秒，也就是2分钟

import pyautogui
import time
from tkinter import Tk
import re


if __name__ == "__main__":
    screenWidth, screenHeight = pyautogui.size() 
    print("scrwidth:{}-scrheight:{}".format(screenWidth, screenHeight))
    time.sleep(3)
    #while(1):
    #    im = pyautogui.screenshot()
    #    print("mouse:{}, color:{}".format(pyautogui.position(), im.getpixel(pyautogui.position())))
    #    time.sleep(.1)

    ############################### way 1 to move and click ################
    pyautogui.click((272, 750))
    pyautogui.click((300, 650)) # click on developer tools
    time.sleep(1)
    pyautogui.click((272, 750))
    pyautogui.click((250, 650)) # click on main chrome window
    time.sleep(3)


    #######################   1  ####################################

############################# method 1 (max ...) ##########################################
    #pyautogui.hotkey('alt', 'tab') 
    #time.sleep(0.5)

    while(1):
        pyautogui.click((1000, 0)) # click on developer tools
        pyautogui.hotkey('ctrl', 'c') 

        data = Tk().clipboard_get()
        #print(data)

        equation = [1, '/', 1, 1]
        equation[0] = re.search(r'="task_x">([0-9]*)', data ,re.IGNORECASE).groups(0)[0]
        equation[1] = re.search(r'"task_op">([^a-z0-9])', data ,re.IGNORECASE).groups(0)[0]    
        equation[2] = re.search(r'="task_y">([0-9]*)', data ,re.IGNORECASE).groups(0)[0]
        equation[3] = int( re.search(r'="task_res">([0-9]*)', data ,re.IGNORECASE).groups(0)[0] )

        if equation[1] == '×':
            equation[1] = '*'
        elif equation[1] == '–':
            equation[1] = '-'

        #print(equation[0], equation[1], equation[2], equation[3])
        #print(eval(equation[0] + equation[1] + equation[2]))

        time.sleep(.001)
        pyautogui.click((100, 5)) # click on main chrome window

        if eval(equation[0] + equation[1] + equation[2]) == equation[3]:
            pyautogui.press('left')
        else:
            pyautogui.press('right')
        
        
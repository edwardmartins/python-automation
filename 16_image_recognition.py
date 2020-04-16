import pyautogui

# Takes an screenshot and save it
pyautogui.screenshot('screen_shot.png')

# Finds an image on the screen
print(pyautogui.locateOnScreen('calc7.png'))

# Finds the center of an image on the screen
x, y = pyautogui.locateCenterOnScreen('calc7.png')

# Moves to the image
pyautogui.moveTo(x,y)

# Clicks into the image
pyautogui.click(x,y)
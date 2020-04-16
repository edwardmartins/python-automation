
import pyautogui

# Tells us the screen resolution
print(pyautogui.size())
width, height = pyautogui.size()

# Returns the current coordinates of the mouse
print(pyautogui.position())

# Moves the mouse
pyautogui.moveTo(500, 500, duration=2)  # absolute position
pyautogui.moveRel(200, 0, duration=2)  # realative(x offset, y offset)
pyautogui.moveRel(0, -100, duration=2)  # 100 hundred pixels up

# Click the mouse
pyautogui.click(20, 1057)
pyautogui.doubleClick()
pyautogui.rightClick()
pyautogui.middleClick()

# Moves and drag the mouse
pyautogui.click()    
distance = 200
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.2)   # move right
    distance = distance - 25
    pyautogui.dragRel(0, distance, duration=0.2)   # move down
    pyautogui.dragRel(-distance, 0, duration=0.2)  # move left
    distance = distance - 25
    pyautogui.dragRel(0, -distance, duration=0.2)  # move up

# Displays the current position of the mouse
pyautogui.displayMousePosition()
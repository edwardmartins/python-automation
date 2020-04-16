import pyautogui

# Moves mouse click and write
pyautogui.click(100,100)
pyautogui.typewrite('Hello world', interval=0.2)

# Send a list of keys to press them
pyautogui.typewrite(['a','b', 'left','left','X', 'Y'], interval=0.2)

# List of string name os the keyboard
print(pyautogui.KEYBOARD_KEYS)

# Press a single key
pyautogui.press('F1')

# Doing a shortcut
pyautogui.hotkey('ctrl','o')


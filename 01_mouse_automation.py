import pyautogui

# Print size of the window
print(pyautogui.size())

# Print the position of the mouse
print(pyautogui.position())

# Move mouse cursor
pyautogui.moveTo(138, 188)
# Move mouse cursor with time
pyautogui.moveTo(222, 222, 2)

# Click
pyautogui.click()
pyautogui.click(button='right')
pyautogui.doubleClick()
pyautogui.click(clicks=3, interval=1)

# Open mouse info program
# pyautogui.mouseInfo()

# Drag
pyautogui.moveTo(1609, 71, 2)
pyautogui.dragTo(1339, 67, 2)
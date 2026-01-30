import pyautogui

# write
pyautogui.write('Hello, ')
pyautogui.write('world!', interval=.25)
pyautogui.write(' : 한글 체크') # not supporting Korean

# press key
pyautogui.press('up')

# press many keys
# pyautogui.hotkey('ctrl', 'c')
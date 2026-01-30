import pyautogui

# Alert but user cannot decide
pyautogui.alert('You wanna start automation?')
pyautogui.moveTo(500, 500, 1)
pyautogui.moveTo(700, 500, 1)
pyautogui.moveTo(500, 500, 1)
pyautogui.moveTo(500, 300, 1)

# Alert and give user a selection
user_selection = pyautogui.confirm(
  text='Continue?', 
  title='Please confirm :)', 
  buttons=['Yes', 'No']
)
if user_selection == 'Yes':
  pyautogui.moveTo(500, 500, 1)
  pyautogui.moveTo(700, 500, 1)
  pyautogui.moveTo(500, 500, 1)
  pyautogui.moveTo(500, 300, 1)
else:
  print("Automation stopped.")
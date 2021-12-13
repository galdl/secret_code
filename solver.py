from pyautogui import press, typewrite, hotkey

for code in range(100):
    typewrite(str(code))
    press('return')

# press('130123456789')

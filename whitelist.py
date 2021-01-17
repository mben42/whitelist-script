import time, keyboard, pyautogui

userlist = open("whitelist.txt", "r")
commandfile = open("command.txt", "r")
command = commandfile.readline()

time.sleep(5) # 5 seconds sleep to go to Minecraft window

for nick in userlist:
    keyboard.write(f"{command} {nick}")
    pyautogui.press('enter')
    pyautogui.press('t')
    time.sleep(1) # 1 second sleep not to trigger anti-spam systems

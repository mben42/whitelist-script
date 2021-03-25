import time, keyboard, pyautogui

userlist = open("whitelist.txt", "r")
commandfile = open("command.txt", "r")
command = commandfile.readline()

time.sleep(5) # 5 seconds sleep to go to Minecraft window

for nick in userlist:
    nick = nick.rstrip("\r\n")
    keyboard.write(f"{command} {nick}")
    pyautogui.press('enter')
    pyautogui.press('t')
    time.sleep(5) # 5 seconds sleep not to trigger anti-spam systems

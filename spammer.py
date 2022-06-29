import pyautogui, time
time.sleep(5)
spamPoruke = open("spam-text.txt", "r")
for poruka in spamPoruke:
    pyautogui.typewrite(poruka)
    pyautogui.press("enter")

spamPoruke.close()
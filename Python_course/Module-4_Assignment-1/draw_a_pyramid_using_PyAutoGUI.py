import pyautogui

n=int(input())
print(n)
for i in range(n+1):
    for j in range(i):
        pyautogui.write('#',interval=0.25)
    pyautogui.press('enter')


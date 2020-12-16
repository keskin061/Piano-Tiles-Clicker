import time
import pyautogui
import win32api
import win32con
from pynput.mouse import Button, Controller
import keyboard

mouse = Controller()


# Tıklama fonksiyonu
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

# x ve y koordinatları
yPosition = 500
x1 = 550
x2 = 650
x3 = 750
x4 = 850


while keyboard.is_pressed("q") == False:
    # Döngüyü durdurmak için q basınız

    try:
        if pyautogui.pixel(x1, yPosition)[0] == 0:
            click(x1, yPosition)
        if pyautogui.pixel(x2, yPosition)[0] == 0:
            click(x2, yPosition)
        if pyautogui.pixel(x3, yPosition)[0] == 0:
            click(x3, yPosition)
        if pyautogui.pixel(x4, yPosition)[0] == 0:
            click(x4, yPosition)
        # Koordinatlardaki piksellerin RGB bilgisinin ilk bilgisi kullanılmış
    except:
        print("Buton bulunamadı")
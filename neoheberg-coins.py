import pyautogui
import time
from PIL import ImageGrab

# Couleurs à checker
color_ignore = "#459F48".lower()
color_trigger = "#FF5722".lower()

print("Détection en cours... Déplace la souris sur la zone à surveiller.")

try:
    while True:
        x, y = pyautogui.position()
        screenshot = ImageGrab.grab(bbox=(x, y, x+1, y+1))  # Prend un pixel sous la souris
        pixel_color = screenshot.getpixel((0, 0))
        hex_color = '#{:02X}{:02X}{:02X}'.format(*pixel_color).lower()

        print(f"Couleur détectée : {hex_color} à ({x},{y})", end='\r')

        if hex_color == color_trigger:
            print(f"\n💥 Trigger couleur détectée ({hex_color}) -> Click !")
            pyautogui.click()
            time.sleep(0.5)  # Anti double click

        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nArrêt manuel du script. ✋")

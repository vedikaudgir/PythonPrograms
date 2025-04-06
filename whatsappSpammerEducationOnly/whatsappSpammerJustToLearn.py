import pyautogui
import time

message = "Hey bro"
count = 100

print("🔥 You have 10 seconds to click on the WhatsApp chat...")
time.sleep(10)

for i in range(count):
    pyautogui.write(message)
    pyautogui.press("enter")
    print(f"Sent {i+1}/{count}")

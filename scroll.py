import pyautogui
import time
try:
    while True:
        # Scroll up
        pyautogui.scroll(100)  # Adjust the value for the amount to scroll
        time.sleep(1)  # Wait for 1 second
        
        # Scroll down
        pyautogui.scroll(-100)  # Adjust the value for the amount to scroll
        time.sleep(1)  # Wait for 1 second
except KeyboardInterrupt:
    print("\nExiting...")  # Graceful exit on keyboard interrupt
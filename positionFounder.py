import pyautogui
import time

try:
    while True:
        position = pyautogui.position()  # Get the mouse position
        print(f"Current mouse position: {position}")  # Print the position
        time.sleep(1)  # Wait for 1 second before updating again
except KeyboardInterrupt:
    print("\nExiting...")  # Graceful exit on keyboard interrupt
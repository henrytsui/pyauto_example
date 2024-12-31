import pyautogui
import keyboard
import threading
import time

# Global variable to track the state of the clicker
clicker_running = False

def click_periodically():
    global clicker_running
    while clicker_running:
        pyautogui.click()
        time.sleep(0.2)  # Adjust the sleep time as needed

def main():
    global clicker_running
    print("Press Ctrl+Enter to start/stop the clicker")
    while True:
        if keyboard.is_pressed('ctrl+enter'):
            clicker_running = not clicker_running
            if clicker_running:
                threading.Thread(target=click_periodically).start()
                print("Clicker started")
            else:
                print("Clicker stopped")

            time.sleep(0.1)  # Debounce delay

if __name__ == "__main__":
    main()
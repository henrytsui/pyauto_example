import pyautogui
import keyboard
import threading
import time

record = False
replay = False

def record_actions():
    global record
    with open('actions.txt', 'w') as file:
        while record:
            action = (time.time(), pyautogui.position(), keyboard.read_event())
            file.write(f"{action[0]},{action[1]},{action[2].name}\n")
            file.flush()  # Flush the file buffer to ensure immediate write
            print(f"Recorded action: {action}")

def start_recording():
    print("Start recording...")
    global record
    record = True
    threading.Thread(target=record_actions).start()

def stop_recording():
    global record
    record = False
    print("Stop recording")

def replay_actions():
    global replay
    with open('actions.txt', 'r') as file:
        for line in file:
            action = line.strip().split(',')
            time.sleep(float(action[0]) - time.time())
            pyautogui.moveTo(eval(action[1]))
            keyboard.write(action[2])
            print(f"Replayed action: {action}")

def start_replay():
    global replay
    replay = True
    threading.Thread(target=replay_actions).start()
    print("Start replaying...")

def stop_replay():
    global replay
    replay = False
    print("Stop replaying")

def main():
    threading.Thread(target=keyboard.wait).start()
    keyboard.add_hotkey('ctrl+enter', start_recording)
    keyboard.add_hotkey('ctrl+enter', stop_recording, args=(), suppress=True)
    keyboard.add_hotkey('ctrl+shift+enter', start_replay)
    keyboard.add_hotkey('ctrl+shift+enter', stop_replay, args=(), suppress=True)

    try:
        while True:
            print("Running...")
            time.sleep(2)  # Wait for 2 seconds before the next action
    except KeyboardInterrupt:
        print("\nExiting...")  # Graceful exit on keyboard interrupt

if __name__ == "__main__":
    main()

import time
import pyautogui
import keyboard
import threading

record = False
replay = False

def record_actions():
    global record
    with open('actions.txt', 'w') as file:
        while record:
            action = (time.time(), pyautogui.position(), keyboard.read_event())
            file.write(f"{action[0]},{action[1].x},{action[1].y},{action[2].name}\n")
            file.flush()  # Flush the file buffer to ensure immediate write
            print(f"Recorded action: {action}")

def start_stop_recording():
    global record
    if record:
        record = False
        print("Stop recording")
    else:
        record = True
        print("Start recording")
        threading.Thread(target=record_actions).start()

def replay_actions():
    global replay
    with open('actions.txt', 'r') as file:
        for line in file:
            if not replay:
                break
            action = line.strip().split(',')
            timestamp, x, y, key = float(action[0]), int(action[1]), int(action[2]), action[3]
            time.sleep(max(0, timestamp - time.time()))
            pyautogui.moveTo(x, y)
            keyboard.write(key)
            print(f"Replayed action: {timestamp}, {x}, {y}, {key}")

def start_stop_replay():
    global replay
    if replay:
        replay = False
        print("Stop replaying")
    else:
        replay = True
        print("Start replaying")
        threading.Thread(target=replay_actions).start()

def main():
    keyboard.add_hotkey('ctrl+enter', start_stop_recording)
    keyboard.add_hotkey('ctrl+shift+enter', start_stop_replay)

    try:
        while True:
            print("Waiting for hotkey...")
            time.sleep(2)  # Wait for 2 seconds before the next action
    except KeyboardInterrupt:
        print("\nExiting...")  # Graceful exit on keyboard interrupt

if __name__ == "__main__":
    main()
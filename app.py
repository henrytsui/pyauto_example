import time
import pyautogui
import keyboard
import threading
from queue import Queue
from pynput import mouse

record = False
replay = False
action_queue = Queue()

# Define a function to handle mouse movement
def on_move(x, y):
    print(f'Mouse moved to ({x}, {y})')

# Define a function to handle mouse click events
def on_click(x, y, button, pressed):
    if pressed:
        print(f'Mouse clicked at ({x}, {y}) with {button}')

# Define a function to handle mouse scroll events
def on_scroll(x, y, dx, dy):
    print(f'Mouse scrolled at ({x}, {y}) with delta ({dx}, {dy})')


def record_mouse_events():
    global record
    def on_move(x, y):
        if record:
            action_queue.put((time.time(), pyautogui.position(), None))
    
    def on_click(x, y, button, pressed):
        if record and pressed:
            action_queue.put((time.time(), pyautogui.position(), button))
    
    with mouse.Listener(on_move=on_move, on_click=on_click) as listener:
        listener.join()

# Start listening to mouse events
with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()
    
def record_keyboard_events():
    global record
    while record:
        event = keyboard.read_event()
        action = (time.time(), pyautogui.position(), event)
        action_queue.put(action)

def write_actions_to_file():
    global record
    with open('actions.txt', 'w') as file:
        while record:
            action = action_queue.get()
            file.write(f"{action[0]},{action[1].x},{action[1].y},{action[2].name if action[2] else 'None'}\n")
            file.flush()  # Flush the file buffer to ensure immediate write
            print(f"Recorded action: {action}")
            action_queue.task_done()

def start_stop_recording():
    global record
    if record:
        record = False
        print("Stop recording")
    else:
        record = True
        print("Start recording")
        keyboard_thread = threading.Thread(target=record_keyboard_events)
        mouse_thread = threading.Thread(target=record_mouse_events)
        writer_thread = threading.Thread(target=write_actions_to_file)
        keyboard_thread.start()
        mouse_thread.start()
        writer_thread.start()

def replay_actions():
    global replay
    with open('actions.txt', 'r') as file:
        round = 0
        while replay:
            cur_action = 0  # Current action number
            file.seek(0)  # Reset the file pointer to the beginning
            for line in file:
                if not replay:
                    break
                action = line.strip().split(',')
                timestamp, x, y, key = float(action[0]), int(action[1]), int(action[2]), action[3]
                time.sleep(max(0, timestamp - time.time()))
                pyautogui.moveTo(x, y)
                if key is not None:
                    keyboard.write(key)
                print(f"Round {round} action {cur_action}: {timestamp}, {x}, {y}, {key}")
                cur_action += 1
            print(f"Round {round} completed")
            round += 1

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

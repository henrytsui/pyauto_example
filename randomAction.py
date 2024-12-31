import pyautogui
import random
import time

# List of functions to randomly call
functions = [
    'moveTo',
    'click',
    'doubleClick',
    'rightClick',
    'scroll',
    'typewrite',
    'screenshot'
]

# Function to execute a random action
def random_action():
    action = random.choice(functions)
    
    # Call the selected function
    if action == 'moveTo':
        x, y = random.randint(0, 1920), random.randint(0, 1080)  # Adjust coordinates for your screen
        print(f'Moving mouse to ({x}, {y})')
        pyautogui.moveTo(x, y, duration=1)
        
    elif action == 'click':
        x, y = pyautogui.position()  # Click at current mouse position
        print(f'Clicking at position ({x}, {y})')
        pyautogui.click(x, y)
        
    elif action == 'doubleClick':
        x, y = pyautogui.position()  # Double-click at current mouse position
        print(f'Double-clicking at position ({x}, {y})')
        pyautogui.doubleClick(x, y)
        
    elif action == 'rightClick':
        x, y = pyautogui.position()  # Right-click at current mouse position
        print(f'Right-clicking at position ({x}, {y})')
        pyautogui.rightClick(x, y)
        
    elif action == 'scroll':
        scroll_amount = random.randint(-100, 100)  # Random scroll amount
        print(f'Scrolling {"up" if scroll_amount > 0 else "down"} by {abs(scroll_amount)}')
        pyautogui.scroll(scroll_amount)
        
    elif action == 'typewrite':
        text = "Hello, this is a random typing action!"
        print(f'Typing: {text}')
        pyautogui.typewrite(text)
        
    elif action == 'screenshot':
        print('Taking a screenshot...')
        screenshot = pyautogui.screenshot()
        screenshot.save('screenshot.png')  # Save screenshot to file

if __name__ == "__main__":
    print("You have 5 seconds to switch to the desired window...")
    time.sleep(5)
    
    try:
        while True:
            random_action()
            time.sleep(2)  # Wait for 2 seconds before the next action
    except KeyboardInterrupt:
        print("\nExiting...")  # Graceful exit on keyboard interrupt
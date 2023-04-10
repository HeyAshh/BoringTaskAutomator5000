import pyautogui
import time
from pynput import keyboard, mouse

# Define the coordinates of the points you want to click
points = []

# Define the delay between clicks in seconds
click_delay = 3

# Define variables to keep track of the automation and mapping states
running = False
mapping = False

# Define a function to start the automation
def start_automation():
    global running
    running = True

# Define a function to pause the automation
def pause_automation():
    global running
    running = False

# Define a function to start the mapping
def start_mapping():
    global mapping
    mapping = True

# Define a function to stop the mapping
def stop_mapping():
    global mapping
    mapping = False

# Define a function to perform actions based on key presses
def on_press(key):
    if key == keyboard.Key.f2:
        start_mapping()
    elif key == keyboard.Key.f3:
        stop_mapping()
    elif key == keyboard.Key.f5:
        start_automation()
    elif key == keyboard.Key.f6:
        pause_automation()
    elif key == keyboard.Key.esc:
        return False

# Define a function to perform actions based on mouse clicks
def on_click(x, y, button, pressed):
    global points
    if mapping and pressed and button == mouse.Button.left:
        points.append((x, y))
        print(f"Added point: ({x}, {y})")

# Create a listener for the key presses
keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()

# Create a listener for the mouse clicks
mouse_listener = mouse.Listener(on_click=on_click)
mouse_listener.start()

while True:
    # Check if the automation is running
    if running:
        for point in points:
            # Click on the point
            pyautogui.click(point)

            # Wait for the specified delay
            time.sleep(click_delay)

    # Check if the keyboard listener has stopped
    if not keyboard_listener.is_alive():
        mouse_listener.stop()
        break

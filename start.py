import Quartz
import AppKit
import pyperclip
import pytesseract
from PIL import Image
import os
import time

def clear_terminal():
    os.system('clear')

def capture_screenshot():
    screenshot_command = "screencapture -i screenshot.png"
    os.system(screenshot_command)

    if not os.path.isfile("screenshot.png"):
        print("No screenshot taken")
        return None

    return "screenshot.png"

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def on_press(key_code, shift_pressed):
    global taking_screenshot

    if shift_pressed and key_code == 18:  # Key code 18 corresponds to '1'
        if not taking_screenshot:
            taking_screenshot = True
            screenshot_path = capture_screenshot()
            if not screenshot_path:
                taking_screenshot = False
                return

            extracted_text = extract_text_from_image(screenshot_path)
            pyperclip.copy(extracted_text)
            print("Text extracted and copied to clipboard")

            # Delete the screenshot file after processing
            if os.path.exists(screenshot_path):
                os.remove(screenshot_path)
                print("Screenshot file deleted")
                print("Press Shift + 2 to restart and take another screenshot")

            taking_screenshot = False

    elif shift_pressed and key_code == 19:  # Key code 19 corresponds to '2'
        clear_terminal()
        display_loading_screen()
        print("Press Shift + 1 to start the screenshot process")

def event_handler(proxy, event_type, event, refcon):
    if event_type == Quartz.kCGEventFlagsChanged or event_type == Quartz.kCGEventKeyDown:
        key_code = Quartz.CGEventGetIntegerValueField(event, Quartz.kCGKeyboardEventKeycode)
        shift_pressed = Quartz.CGEventGetFlags(event) & Quartz.kCGEventFlagMaskShift
        on_press(key_code, shift_pressed)
    return event

def display_loading_screen():
    clear_terminal()
    print("""
___________              __            _________ .__  .__        
\__    ___/___ ___  ____/  |_          \_   ___ \|  | |__|_____  
  |    |_/ __ \\  \/  /\   __\  ______ /    \  \/|  | |  \____ \ 
  |    |\  ___/ >    <  |  |   /_____/ \     \___|  |_|  |  |_> >
  |____| \___  >__/\_ \ |__|            \______  /____/__|   __/ 
             \/      \/                        \/        |__|        """)
    time.sleep(0.5)
    print("Developed by JewlzEncrypted")
    time.sleep(0.5)
    print("github.com/jewlzencrypted")
    time.sleep(0.5)

def main():
    global taking_screenshot
    taking_screenshot = False
    display_loading_screen()
    print("Press Shift + 1 to start the screenshot process")

    event_mask = (
        Quartz.kCGEventMaskForAllEvents |
        Quartz.kCGEventKeyDown |
        Quartz.kCGEventFlagsChanged
    )

    event_tap = Quartz.CGEventTapCreate(
        Quartz.kCGHIDEventTap,
        Quartz.kCGHeadInsertEventTap,
        Quartz.kCGEventTapOptionDefault,
        event_mask,
        event_handler,
        None
    )

    if not event_tap:
        print("Failed to create event tap.")
        return

    run_loop_source = Quartz.CFMachPortCreateRunLoopSource(None, event_tap, 0)
    Quartz.CFRunLoopAddSource(
        Quartz.CFRunLoopGetCurrent(),
        run_loop_source,
        Quartz.kCFRunLoopDefaultMode
    )
    Quartz.CGEventTapEnable(event_tap, True)

    AppKit.NSApplication.sharedApplication().run()

if __name__ == "__main__":
    main()

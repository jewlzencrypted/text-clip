Text Clip
Text Clip is a simple yet powerful Python-based tool designed to streamline the process of capturing and extracting text from screenshots. Developed with ease of use in mind, Text Clip allows users to quickly take a screenshot, extract the text content, and copy it directly to their clipboard for immediate use.

Features
Quick Screenshot Capture: Initiate the screenshot process by pressing Shift + 1. Drag to select the area of the screen you want to capture.
Automatic Text Extraction: Utilizes OCR (Optical Character Recognition) to convert the captured screenshot into text.
Clipboard Integration: The extracted text is automatically copied to your clipboard, ready to be pasted wherever you need it.
Easy Re-capture: After taking a screenshot, press Shift + 2 to restart the process and take another screenshot without restarting the application.
User-Friendly Interface: Clear terminal display with instructions and feedback messages to guide you through the process.
How It Works
Run the Script: Start the application by running the Python script.
Follow On-Screen Instructions: After a brief loading screen, you will see instructions to press Shift + 1 to start the screenshot process.
Capture the Screenshot: Use your mouse to select the area of the screen you want to capture.
Text Extraction and Copy: The application extracts the text from the screenshot and copies it to your clipboard.
Re-capture if Needed: If you want to take another screenshot, press Shift + 2 to restart the process.
Requirements
Python 3.x
Required Python libraries:
Quartz
AppKit
pyperclip
pytesseract
pillow (PIL)
Installation
Make sure you have the necessary libraries installed. You can install them using pip:

sh
Copy code
pip install pyobjc pyobjc-framework-Quartz pyperclip pytesseract pillow
Usage
Clone the repository and navigate to the directory:

sh
Copy code
git clone https://github.com/jewlzencrypted/text-clip.git
cd text-clip
Run the script:

sh
Copy code
python start.py
Follow the on-screen instructions to capture your screenshot and extract the text.

Contributing
Feel free to fork this repository and submit pull requests. Your contributions are welcome!

License
This project is licensed under the MIT License.


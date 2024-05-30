# Text Clip

**Text Clip** is a simple yet powerful Python-based tool designed to streamline the process of capturing and extracting text from screenshots. Developed with ease of use in mind, Text Clip allows users to quickly take a screenshot, extract the text content, and copy it directly to their clipboard for immediate use.

## Features

- **Quick Screenshot Capture**: Initiate the screenshot process by pressing `Shift + 1`. Drag to select the area of the screen you want to capture.
- **Automatic Text Extraction**: Utilizes OCR (Optical Character Recognition) to convert the captured screenshot into text.
- **Clipboard Integration**: The extracted text is automatically copied to your clipboard, ready to be pasted wherever you need it.
- **Easy Re-capture**: After taking a screenshot, press `Shift + 2` to restart the process and take another screenshot without restarting the application.
- **User-Friendly Interface**: Clear terminal display with instructions and feedback messages to guide you through the process.

## How It Works

1. **Run the Script**: Start the application by running the Python script.
2. **Follow On-Screen Instructions**: After a brief loading screen, you will see instructions to press `Shift + 1` to start the screenshot process.
3. **Capture the Screenshot**: Use your mouse to select the area of the screen you want to capture.
4. **Text Extraction and Copy**: The application extracts the text from the screenshot and copies it to your clipboard.
5. **Re-capture if Needed**: If you want to take another screenshot, press `Shift + 2` to restart the process.

## Requirements

- Python 3.11
- Required Python libraries:
  - Quartz
  - AppKit
  - pyperclip
  - pytesseract
  - pillow (PIL)

## Installation

Make sure you have the necessary libraries installed. You can install them using pip:


pip install pyobjc pyobjc-framework-Quartz pyperclip pytesseract pillow

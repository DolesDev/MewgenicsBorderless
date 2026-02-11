# Mewgenics Borderless Fix
A utility to force the game into borderless fullscreen mode.

> **Note on Antivirus:** This tool may trigger a warning from Windows Defender or other antivirus software. This happens because the script uses Windows API calls to modify another window's properties. The project is open source so the code can be inspected for safety.

## Usage
1. Open Mewgenics and set the display to Windowed mode
2. Run MewgenicsBorderless.exe
3. Enjoy!

## Requirements for source
If running from the .py file, you must install the following:
pywin32

## How it works
The script uses the Windows API to identify the game window, remove the title bar and borders, and resize the window to match your primary monitor's dimensions

## Disclaimer
This is a fan-made tool. It is not affiliated with or endorsed by Edmund McMillen or Tyler Glaiel

## License
MIT License

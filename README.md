# partial-screenshotter
Lightweight script that allows the user to select an area of the screen to capture in a screenshot. Designed for integration with AutoHotkey on Windows as a replacement to Windows' screenshoot tools, which annoyingly require several steps to use. This script was designed to be as simple to use and lightweight as possible.

Use: 

Once installed, simply press the key of your choice to start the script. When you see the cursor change to a cross, click and drag to select the area you want to capture. It's immediately sent to the desktop and the script closes. 

Installation:

1) Ensure the pyautogui package is installed.
2) Edit download_path in the python file so it contains your Windows username.
3) Edit the paths for your Python instllation and the script in the provided ahk file.
4) Run the provided AutoHotkey file to bind the script to your Pause key.

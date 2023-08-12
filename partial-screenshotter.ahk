#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
Pause::
Run, C:\Users\YOURUSERNAMEHERE\AppData\Local\Programs\Python\Python311\pythonw.exe "C:\PATHTOFOLDER\partial-screenshotter\partial-screenshotter.pyw"
return

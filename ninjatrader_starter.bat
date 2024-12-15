del /q "%USERPROFILE%\Documents\NinjaTrader 8\cache\*.*"
for /d %%F in ("%USERPROFILE%\Documents\NinjaTrader 8\cache\*") do rd /s /q "%%F"

del /q "%USERPROFILE%\Documents\NinjaTrader 8\db\cache\*.*"
for /d %%F in ("%USERPROFILE%\Documents\NinjaTrader 8\db\cache\*") do rd /s /q "%%F"

"%ProgramFiles%\NinjaTrader 8\bin\NinjaTrader.exe"

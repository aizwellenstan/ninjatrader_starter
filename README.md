# NINJATRADER Starter

```ninjatrader_starter.py
import os
import subprocess

# Clear NinjaTrader cache
os.system('del /q "%USERPROFILE%\\Documents\\NinjaTrader 8\\cache\\*.*"')
os.system('for /d %F in ("%USERPROFILE%\\Documents\\NinjaTrader 8\\cache\\*") do rd /s /q "%F"')

os.system('del /q "%USERPROFILE%\\Documents\\NinjaTrader 8\\db\\cache\\*.*"')
os.system('for /d %F in ("%USERPROFILE%\\Documents\\NinjaTrader 8\\db\\cache\\*") do rd /s /q "%F"')

# Launch NinjaTrader
subprocess.Popen(r'"C:\Program Files\NinjaTrader 8\bin\NinjaTrader.exe"')
```

```
python -m pip install pyinstaller
pyinstaller --onefile --icon="C:\Program Files\NinjaTrader 8\bin\NinjaTrader.ico" ninjatrader_starter.py
```

### bat ver.
```
del /q "%USERPROFILE%\Documents\NinjaTrader 8\cache\*.*"
for /d %%F in ("%USERPROFILE%\Documents\NinjaTrader 8\cache\*") do rd /s /q "%%F"

del /q "%USERPROFILE%\Documents\NinjaTrader 8\db\cache\*.*"
for /d %%F in ("%USERPROFILE%\Documents\NinjaTrader 8\db\cache\*") do rd /s /q "%%F"

"%ProgramFiles%\NinjaTrader 8\bin\NinjaTrader.exe"
```

import os
import subprocess

# Clear NinjaTrader cache
os.system('del /q "%USERPROFILE%\\Documents\\NinjaTrader 8\\cache\\*.*"')
os.system('for /d %F in ("%USERPROFILE%\\Documents\\NinjaTrader 8\\cache\\*") do rd /s /q "%F"')

os.system('del /q "%USERPROFILE%\\Documents\\NinjaTrader 8\\db\\cache\\*.*"')
os.system('for /d %F in ("%USERPROFILE%\\Documents\\NinjaTrader 8\\db\\cache\\*") do rd /s /q "%F"')

# Launch NinjaTrader
subprocess.Popen(r'"C:\Program Files\NinjaTrader 8\bin\NinjaTrader.exe"')

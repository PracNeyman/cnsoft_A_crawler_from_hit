@echo on

start/wait python getIP.py
pause
start/wait python master.py
pause
for /l %%i in (1,1,8) do (
start python slaver.py
)
pause
start py -3 -m generateCSV.py
exit
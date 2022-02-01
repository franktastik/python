import os
import psutil

python_process = psutil.getloadavg()
python_process1 = psutil.cpu_count(logical=False) 
p= psutil.cpu_times()

print('\nCPU\n---')
print('\nload average\n------------')
print('------------   ------------   --------')
print(python_process)
print('\ncores\n-----')
print('-')
print(python_process1)
print('-')
print('\ntimes\n------')
print(p)

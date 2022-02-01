# python
Collecting metrics.

### Install psutil
  > pip install psutil

### To use get the Memory metrics, use the psutil
  > psutil.virtual_memory()
  > 
  > psutil.swap_memory()

### To collect cpu metrics
  > psutil.getloadavg()
  > 
  > psutil.cpu_count(logical=False) 
  > 
  > psutil.cpu_times()

### To run the task on your system, use the python command
  > python3 <filename.py> 

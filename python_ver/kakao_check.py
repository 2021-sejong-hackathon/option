import psutil
print([p.name() for p in psutil.process_iter()])
import os
import time

now = time.time()
for foldername, subfolders, filenames in os.walk(os.getcwd()):
    for filename in filenames:
        filepath = os.path.abspath(filename)
        if os.path.getsize(filepath) > 2**20 and os.stat(filepath).st_mtime < now - 7 * 86400::
            print(filepath)

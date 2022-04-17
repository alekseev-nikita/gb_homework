import os
from collections import defaultdict


root_dir = '/home/kch/Downloads'
downloads_dir = defaultdict(int)
for root, dirs, files in os.walk(root_dir):
    for file in files:
        file_path = os.path.join(root, file)
        if os.path.getsize(file_path) < 100:
            downloads_dir[100] += 1
            continue
        elif os.path.getsize(file_path) < 1000:
            downloads_dir[1000] += 1
            continue
        elif os.path.getsize(file_path) < 10000:
            downloads_dir[10000] += 1
            continue
        elif os.path.getsize(file_path) < 100000:
            downloads_dir[100000] += 1
        continue
print(downloads_dir)

import os


def structure():
    project_name = None
    hierarchy_dirs = set()
    hierarchy_files = set()
    current_dir = []
    with open('config.yaml', 'r', encoding='UTF-8') as f:
        for line in f:
            line = line.strip()
            separator_counter = line.count('|')
            if separator_counter == 0:
                project_name = line.replace('--', '')
                continue
            line = line.split('|--')[-1]
            if separator_counter > len(current_dir):
                current_dir.append(line)
            elif separator_counter == len(current_dir):
                current_dir[separator_counter - 1] = line
            else:
                t_dir = []
                for idx in range(separator_counter):
                    if idx < separator_counter - 1:
                        t_dir.append(current_dir[idx])
                    else:
                        t_dir.append(line)
                current_dir = t_dir
            hierarchy_dirs.add(os.path.join(project_name, *current_dir)) if '.' not in line \
                else hierarchy_files.add(os.path.join(project_name, *current_dir))

    return hierarchy_dirs, hierarchy_files


directories, files = structure()

for d in directories:
    try:
        os.makedirs(d)
    except FileExistsError:
        continue
for f in files:
    with open(f, 'a'): pass

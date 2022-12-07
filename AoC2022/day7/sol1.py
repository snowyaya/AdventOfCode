import sys
import os
import collections

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    data = f.read().strip()
    
raw_commands = data.split('$ ')[1:]
command_output_lines = [
    [x for x in raw_command.split('\n') if len(x)] for raw_command in raw_commands
]
# print(new_lines)

commands = [
    {
        "command": line[0],
        "output": line[1:]
    }
    for line in command_output_lines
]

directories = collections.defaultdict(list)
cwd = "/"
for command in commands:
    command_parts = command["command"].split(' ')
    command_name = command_parts[0]
    argument = command_parts[1] if len(command_parts) > 1 else None
    output = command["output"]
    
    if command_name == "cd":
        if argument == "/":
            cwd = "/"
            continue
        
        if argument == "..":
            print(cwd)
            cwd = ("/" + "/".join(cwd.split("/")[0:-2]) + "/").replace("//", "/")
            continue
        
        cwd += f"{argument}/"
        cwd.replace('//', '/')
    
    if command_name == "ls":
        for line in output:
            raw_size, name = line.split(' ')
            
            if raw_size == "dir":
                directories[cwd].append(
                    {
                        "type": "dir",
                        "size": None,
                        "name": name
                        }
                )
                continue
            size = int(raw_size)
            directories[cwd].append(
                {
                    "type": "file",
                    "size": size,
                    "name": name,
                }
            )
# print(list(directories.keys()))
def get_recursive_size(folder_name):
    return sum(
        item["size"] if item["type"] == "file" 
        else get_recursive_size(folder_name + item["name"] + "/")
        for item in directories[folder_name] 
    )

# print(list(directories.keys()))

# folders_recursive_size = [
#     get_recursive_size(folder_name)
#     for folder_name in directories.keys()
# ]
# print(sum(size for size in folders_recursive_size if size <= max_folder_size))


folders_recursive_sizes = {
    folder_name: get_recursive_size(folder_name)
    for folder_name in directories.keys()
}

max_folder_size = 100000
total_fs_size = 70000000
total_unused_size = total_fs_size - folders_recursive_sizes["/"]
to_free_up = 30000000 - total_unused_size
print(min(
    [x for x in folders_recursive_sizes.items() if x[1] >= to_free_up],
    key = lambda item: item[1]
))
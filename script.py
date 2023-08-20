import os
temp = '/Users/misakavagyan/test'


with open('results', 'w') as f:
    files = os.listdir(temp)
    for file in sorted(files):
        file_path = os.path.join(temp, file)
        if os.path.isfile(file_path):
            with open(file_path, "r", encoding="latin") as r_file:
                status_file = r_file.read()
                status_line = [line for line in status_file.split('\n') if "Status:" in line]
                if status_line:
                    status = status_line[0].strip()
                    f.write(f"{file} - {status}\n")

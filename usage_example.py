from bash import Bash

Bash.run("find . -name *.py")

print(f"cmd:\n{Bash.command}")
print(f"\nstdout:\n{Bash.stdout}")
print(f"\nstderr:\n{Bash.stderr}")
print(f"\nreturn code:\n{Bash.rc}")

files_found_list = list(Bash.stdout.strip().split('\n'))

for file in files_found_list:
    Bash.run(f'ls -l {file}', capture_output=False)

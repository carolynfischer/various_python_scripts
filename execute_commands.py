"""
Subprocess example
"""
import subprocess 

def execute_commands():
    proc = subprocess.Popen(['echo', 'Hello from subprocess'], stdout=subprocess.PIPE)
    out, err = pro.communicate()
    print out.decode('utf-8')

if __name__ == "__main__":
    execute_commands()
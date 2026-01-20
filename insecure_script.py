import subprocess
import shlex

user_input = input("Enter command: ")
subprocess.run(shlex.split(user_input))

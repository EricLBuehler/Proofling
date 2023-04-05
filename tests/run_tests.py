import subprocess
from os import system, name
subprocess.run(["pip", "install", "pytest"])
subprocess.run(["pip", "install", "-e", "."])
print("\nPackages successfully installed!")
if name == "nt":
    system('cls')
else:
    system('clear')
subprocess.run(["python3", "-m", "pytest", "tests", "-s"])
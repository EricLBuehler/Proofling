import subprocess
from os import system, name, chdir
chdir("../")
subprocess.run(["pip", "install", "-e", "."])
chdir("tests")
print("\nPackages successfully installed!")
if name == "nt":
    system('cls')
else:
    system('clear')
subprocess.run(["python3", "-m", "pytest", "-s"])
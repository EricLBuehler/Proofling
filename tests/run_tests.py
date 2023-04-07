#Run in this tests directory
import subprocess
import os

os.chdir("../")
subprocess.run(["pip", "install", "-e", "."])
os.chdir("tests")
print("\nPackages successfully installed!")

if os.name == "nt":
    os.system('cls')
else:
    os.system('clear')
    
subprocess.run(["python3", "-m", "pytest", "-s"])
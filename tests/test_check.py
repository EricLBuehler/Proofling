from proofling import proofling
import os

def test_check():
    os.chdir("tests")
    with open("proof1.txt", "r") as file:
        text = file.read()

    print(text)
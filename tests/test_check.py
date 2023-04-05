from proofling.proofling import Proofling
import os

def test_check():
    print()
    with open("proof1.txt", "r") as file:
        text = file.read()
    
    text = """
    {
    p = A
    q = B
    }

    (p > q, p) : q
    """
    proofling = Proofling()
    proofling.check(text)
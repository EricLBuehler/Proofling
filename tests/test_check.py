from proofling.proofling import Proofling

def test_with_value():
    print()
    with open("proof_value.txt", "r") as file:
        text = file.read()

    proofling = Proofling()
    assert proofling.check(text), "should be True"

def test_with_no_value():
    print()
    with open("proof_no_value.txt", "r") as file:
        text = file.read()
        
    proofling = Proofling()
    assert proofling.check(text), "should be True"
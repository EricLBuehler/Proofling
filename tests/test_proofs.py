from proofling.proofling import Proofling

def _test_with_value():
    print("\n\nTest with value")
    with open("proof_value.txt", "r") as file:
        text = file.read()

    proofling = Proofling()
    assert proofling.check(text), "should be True"

def _test_with_no_value():
    print("\n\nTest with no value")
    with open("proof_no_value.txt", "r") as file:
        text = file.read()
        
    proofling = Proofling()
    assert proofling.check(text), "should be True"

def test_simple_proof():
    print("\n\nTest with simple proof")
    with open("proof_simple.txt", "r") as file:
        text = file.read()
        
    proofling = Proofling()
    assert proofling.check(text), "should be True"
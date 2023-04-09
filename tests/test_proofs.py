from proofling.proofling import Proofling

def test_with_value():
    print("\n\nTest proof with proposition that has a value:")
    with open("proof_value.txt", "r") as file:
        text = file.read()

    proofling = Proofling()
    assert proofling.check(text), "should be True"
    print("\033[1mTest proof with value: ✅")

def test_with_no_value():
    print("\n\nTest proof with proposition that has no value:")
    with open("proof_no_value.txt", "r") as file:
        text = file.read()
        
    proofling = Proofling()
    assert proofling.check(text), "should be True"
    print("\033[1mTest proof with proposition that has no value: ✅")

def test_simple_proof():
    print("\n\nTest with simple proof:")
    with open("proof_simple.txt", "r") as file:
        text = file.read()
        
    proofling = Proofling()
    assert proofling.check(text), "should be True"
    print("\033[1mTest simple proof: ✅")
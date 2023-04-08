from enum import Enum
import typing
import proofling.proof_blocks.proof_blocks as proof_blocks    

# Proposition linkers
class LinkageType(Enum):
    IMPLIES = 0

    @staticmethod
    def create(parent: proof_blocks.Proposition):
        if isinstance(parent, proof_blocks.Implies):
            return LinkageType.IMPLIES
        raise TypeError(f"{type(parent)} is not a valid proposition to get type.")

class PropositionLinkage:
    def __init__(self, parent: proof_blocks.Block, propsition: proof_blocks.Proposition):
        self.parent = parent
        self.proposition = propsition
        self.tp = LinkageType.create(self.parent)

    def __repr__(self):
        return f"PropositionLinkage: {self.proposition} of {self.parent}"

class PropositionLinkageTree:
    def __init__(self):
        self.tree: typing.List[PropositionLinkage] = []

    @staticmethod
    def create(lines: typing.List[proof_blocks.Block]):
        tree = PropositionLinkageTree()
        return tree
    
    def __repr__(self):
        return str(self.tree)
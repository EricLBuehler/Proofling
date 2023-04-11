from enum import Enum
import typing
import proofling.proof_blocks.proof_blocks as proof_blocks    

# Proposition linkers
class LinkageType(Enum):
    IMPLIES = 0
    COMBINED = 1
    THEREFORE = 2

    @staticmethod
    def create(parent: proof_blocks.Proposition):
        if isinstance(parent, proof_blocks.Implies):
            return LinkageType.IMPLIES
        elif isinstance(parent, proof_blocks.Combined):
            return LinkageType.COMBINED
        elif isinstance(parent, proof_blocks.Therefore):
            return LinkageType.THEREFORE
        raise TypeError(f"{type(parent)} is not a valid proposition to get type.")

class PropositionLinkage:
    def __init__(self, parents: typing.List[proof_blocks.Block], propsition: proof_blocks.Proposition, index: int):
        self.parents = parents
        self.proposition = propsition
        self.tps = [LinkageType.create(parent) for parent in parents]
        self.index = index

    def __repr__(self):
        return f"PropositionLinkage: {self.proposition} of {self.tps} at index '{self.index}'"

class PropositionLinkageTree:
    def __init__(self):
        self._tree: typing.List[PropositionLinkage] = []

    def get_tree(self) -> typing.List[PropositionLinkage]:
        return self._tree
    
    tree = property(get_tree)

    @staticmethod
    def create(lines: typing.List[proof_blocks.Block]):
        tree = PropositionLinkageTree()
        for proposition in proof_blocks.Proposition.propositions:
            for line in lines:
                if  (isinstance(line, proof_blocks.BinaryBlock) and line.contains(proposition, [line])[0]) or \
                    isinstance(line, proof_blocks.Combined) and line.contains(proposition, [line])[0]:
                    tree.append(PropositionLinkage(line.contains(proposition, [line])[1][2:], proposition, line.get_index(proposition)))

        return tree

    def append(self, linkage):
        self._tree.append(linkage)

    def __repr__(self):
        return str(self.tree)
    
    def __len__(self):
        return len(self._tree)
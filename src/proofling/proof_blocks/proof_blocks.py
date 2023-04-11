import typing
import proofling.errors.errors as errors
import string        
import abc

#Multi-file state static class
class ParserState:
    combined = False
    proposition_stop = False
    last_proposition = False

    def in_combined() -> bool:
        return ParserState.combined
    
    def set_combined(value: bool):
        ParserState.combined = value

    def in_proposition_stop() -> bool:
        return ParserState.proposition_stop
    
    def set_proposition_stop(value: bool):
        ParserState.proposition_stop = value

    def in_last_proposition() -> bool:
        return ParserState.last_proposition
    
    def set_last_proposition(value: bool):
        ParserState.last_proposition = value

def parse_next(line_gen):
    match next(line_gen):
        case "(":
            return Combined.generate(line_gen)
            
        case other:
            if other in string.ascii_letters:
                return Proposition.generate(Proposition(other), line_gen)
            raise errors.LineSyntaxError(f"Expected '(' or an alphabetic symbol: '{other}'")

#Basic block superclasses
class Block(abc.ABC):
    @abc.abstractmethod
    def contains(self, other, parent):
        pass
    
    @abc.abstractmethod
    def get_index(self, other):
        pass

class BinaryBlock(Block):
    def __init__(self, p: Block, q: Block, name: str):
        self.p, self.q = p, q
        self.name = name

    def contains(self, other, _):
        if self.p.contains(other, self)[0]:
            return self.p.contains(other, self)
        elif self.q.contains(other, self)[0]:
            return self.q.contains(other, self)
        return [False, None]
        
    def get_index(self, other):
        if (not self.p.contains(other, self)[0]) and (not self.q.contains(other, self)[0]):
            return None
        
        if self.p.contains(other, self)[0]:
            return 0
        return 1
        
    def __repr__(self):
        return f"{self.name}: ({self.p}, {self.q}) at {hex(id(self))}"

#Other 'nodes'
class Combined(Block):
    def __init__(self, blocks: typing.List[Block]):
        self.blocks = blocks

    @staticmethod
    def generate(line_gen):
        ParserState.set_combined(True)
        blocks = []
        cur = ","
        while cur == ",":
            blocks.append(parse_next(line_gen))
            cur = next(line_gen)
        next(line_gen) #skip )
        ParserState.set_combined(False)
        cur = next(line_gen) #should come upon :
        if cur != ":":
            raise errors.LineSyntaxError(f"Expected ':': '{cur}'")
        return Therefore(Combined(blocks), parse_next(line_gen))
        
    def contains(self, other, _):
        if not any([block.contains(other, self)[0] for block in self.blocks]):
            return False

        return [block.contains(other, self)[0] for block in self.blocks].find(True).contains(other)
        
    def get_index(self, other):
        if not any([block.contains(other)[0] for block in self.blocks]):
            return None
        
        return [block.contains(other)[0] for block in self.blocks].find(True)        
        
    def __repr__(self):
        return ",".join([str(block) for block in self.blocks])

class Implies(BinaryBlock):
    def __init__(self, p: Block, q: Block):
        super().__init__(p, q, "Implies")

class Therefore(BinaryBlock):
    def __init__(self, p: Block, q: Block):
        super().__init__(p, q, "Therefore")

class Conjunction(BinaryBlock):
    def __init__(self, p: Block, q: Block):
        super().__init__(p, q, "Conjunction")

class Disjunction(BinaryBlock):
    def __init__(self, p: Block, q: Block):
        super().__init__(p, q, "Disjunction")

class Proposition(Block):
    propositions = []

    def __init__(self, name: str):
        self.name = name

        if self in self.propositions:
            self = self.propositions[self.propositions.index(self)]
        else:
            self.propositions.append(self)
            
    def generate(self, line_gen):
        ParserState.set_proposition_stop(True)
        cur = next(line_gen)
        ParserState.set_proposition_stop(False)
        match cur:
            case ">":
                return Implies(self, parse_next(line_gen))
            
            case "&":
                return Conjunction(self, parse_next(line_gen))
            
            case "|":
                return Disjunction(self, parse_next(line_gen))
                
            case other:
                if (other == "," and ParserState.in_combined()) or ParserState.in_last_proposition():
                    return self
                raise errors.ParseSyntaxError(f"Expected '>', '&', or '|': '{other}'")
        
    def contains(self, other, parent):
        return [self==other, parent]
    
    def get_index(self, _):
        return None
        
    def __repr__(self):
        return f"Proposition '{self.name}' at {hex(id(self))}"

    def __eq__(self, other):
        return self.name == other.name
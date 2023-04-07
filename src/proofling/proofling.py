import typing
import proofling.errors.errors as errors
import proofling.proof_blocks.proof_blocks as proof_blocks

class Proofling:
    def __init__(self):
        self.names: typing.Mapping[str, str] = {}

    def __parse_names(self, names: typing.List[str]) -> typing.List[proof_blocks.Proposition]:
        for name_full in names:            
            #Add to names and proposition collections
            #This allows for propositions with no values
            value = name_full[name_full.index("=")+1:].strip() if name_full.find("=")>=0 else None
            name = name_full[:name_full.index("=")].strip() if name_full.find("=")>=0 else name_full
            self.names[name] = value
            proof_blocks.Proposition(name)

        return proof_blocks.Proposition.propositions
    
    @staticmethod
    def __line_generator(line: str) -> str:
        for char in line:
            if char.isspace():
                continue
            yield char
        
        #This covers the case where a propositon 'letter' is the last char
        while proof_blocks.ParserState.in_proposition_stop():
            proof_blocks.ParserState.set_last_proposition(True)
            yield char
        proof_blocks.ParserState.set_last_proposition(False)

    def __parse_lines(self, proof: str) -> typing.List[proof_blocks.Block]:
        # 1st, strip whitespace from all lines. 2nd, filter out empty lines
        lines_str = list(filter(lambda s: s!="", [s.strip() for s in proof.split("\n")]))

        if lines_str.index("{")<0 or lines_str.index("}")<0: 
            raise errors.ParseError("Expected proper name declaration are bounded by { ... }")

        names = self.__parse_names(lines_str[lines_str.index("{")+1:lines_str.index("}")])
        print(names) #DEBUG

        lines: typing.List[proof_blocks.Block] = []
        for line in lines_str[lines_str.index("}")+1:]:
            print(line) #DEBUG
            line_gen = self.__line_generator(line)
            lines.append(proof_blocks.parse_next(line_gen))
            
        return lines
    
    def check(self, proof: str) -> bool:
        lines = self.__parse_lines(proof)
        
        print(lines) #DEBUG

        return True
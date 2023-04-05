import typing
import proofling.errors.errors as errors
import proofling.proof_blocks.proof_blocks as proof_blocks

class Proofling:
    def __init__(self):
        self.names: typing.Mapping[str, str] = {}

    def __parse_names(self, names: typing.List[str]) -> typing.List[proof_blocks.Proposition]:
        for name in names:            
            #Add to names and proposition collections
            self.names[name[:name.index("=")].strip()] = name[name.index("=")+1:].strip()
            proof_blocks.Proposition(name[:name.index("=")].strip())

        return proof_blocks.Proposition.propositions
    
    @staticmethod
    def __line_generator(line: str) -> str:
        for char in line:
            if char.isspace():
                continue
            yield char
        while proof_blocks.ParserState.in_proposition_stop():
            proof_blocks.ParserState.set_last_proposition(True)
            yield char
        proof_blocks.ParserState.set_last_proposition(False)

    def __parse_lines(self, lines_strs: typing.List[str]) -> typing.List[proof_blocks.Block]:
        lines: typing.List[proof_blocks.Block] = []
        for line in lines_strs:
            print(line)
            line_gen = self.__line_generator(line)
            lines.append(proof_blocks.parse_next(line_gen))
            
        return lines
    
    def check(self, proof: str) -> bool:
        lines_str = list(filter(lambda s: s!="", [s.strip() for s in proof.split("\n")]))

        if lines_str.index("{")<0 or lines_str.index("}")<0:
            raise errors.ParseError("Expected proper name declaration are bounded by { ... }")

        lines = self.__parse_lines(lines_str[lines_str.index("}")+1:])
        print(lines)

        names = self.__parse_names(lines_str[lines_str.index("{")+1:lines_str.index("}")])
        print(names)

        return True
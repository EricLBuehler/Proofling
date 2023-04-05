class ProoflingError(Exception):
    pass

class ParseError(ProoflingError, SyntaxError):
    pass

class NameSyntaxError(ParseError):
    pass

class LineSyntaxError(ParseError):
    pass

class ParseSyntaxError(ParseError):
    pass
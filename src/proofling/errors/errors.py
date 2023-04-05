#Superclass for identification of a ProoflingError
class ProoflingError(Exception):
    pass

#Parsing errors
class ParseError(ProoflingError, SyntaxError):
    pass

class NameSyntaxError(ParseError):
    pass

class LineSyntaxError(ParseError):
    pass

class ParseSyntaxError(ParseError):
    pass
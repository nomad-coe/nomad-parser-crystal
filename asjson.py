from crystalparser import CrystalParser
from nomadcore.parser_backend import JsonParseEventsWriterBackend
import sys

paths=sys.argv[1:]
sys.argv = []
for path in paths:
    # 1. Initialize a parser by giving a path to the CRYSTAL output file and a list of
    # default units
    #path = "test/examples/NaCl/NaCl.out"
    print("Parsing: " + path)
    parser = CrystalParser(path, default_units=["eV"], backend=JsonParseEventsWriterBackend)
    # 2. Parse
    parser.parse()














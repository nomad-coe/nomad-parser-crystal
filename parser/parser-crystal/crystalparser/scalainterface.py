"""
This is the access point to the parser for the scala layer in the
nomad project.
"""
from __future__ import absolute_import
import sys
from . import setup_paths
from nomadcore.parser_backend import JsonParseEventsWriterBackend
from crystalparser import CrystalParser


if __name__ == "__main__":

    # Initialise the parser with the main filename and a JSON backend
    main_file = sys.argv[1]
    parser = CrystalParser(main_file, backend=JsonParseEventsWriterBackend)
    parser.parse()

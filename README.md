This is the main repository of the [NOMAD](http://nomad-lab.eu) parser for
[Crystal](http://www.crystal.unito.it/index.php).

# Installation
This parser is a submodule of the nomad-lab-base repository. Developers within
the NoMaD project will automatically get a copy of this repository when they
download and install the base repository.

# Structure
The scala layer can access the parser functionality through the
scalainterface.py file, by calling the following command:

```python
    python scalainterface.py path/to/main/file
```

This scala interface is separated into it's own file to separate it from the
rest of the code. Some parsers will have the interface in the same file as the
parsing code, but I feel that this is a cleaner approach.

The parser is designed to support multiple versions of Crystal with a [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)
approach: The initial parser class is based on Crystal14, and other versions
will be subclassed from it. By sublassing, all the previous functionality will
be preserved, new functionality can be easily created, and old functionality
overridden only where necesssary.

# Standalone Mode
The parser is designed to be usable also outside the NoMaD project as a
separate python package. This standalone python-only mode is primarily for
people who want to easily access the parser without the need to setup the whole
"NOMAD Stack". It is also used when running custom unit tests found in the
folder "cp2k/test/unittests". Here is an example of the call syntax:

```python
    from crystalparser import CrystalParser
    import matplotlib.pyplot as mpl

    # 1. Initialize a parser by giving a path to the CP2K output file and a list of
    # default units
    path = "path/to/main.file"
    default_units = ["eV"]
    parser = CP2KParser(path, default_units=default_units)

    # 2. Parse
    results = parser.parse()

    # 3. Query the results with using the id's created specifically for NOMAD.
    scf_energies = results["energy_total_scf_iteration"]
    mpl.plot(scf_energies)
    mpl.show()
```

# Tools and Methods
This section describes some of the guidelines that are used in the development
of this parser.

## Documentation
This parser follows the [google style
guide](https://google.github.io/styleguide/pyguide.html?showone=Comments#Comments)
for documenting python code. Documenting makes it much easier to follow the
logic behind your parser.

## Testing
The parsers can become quite complicated and maintaining them without
systematic testing is impossible. There are general tests that are
performed automatically in the scala layer for all parsers. This is essential,
but can only test that the data is outputted in the correct format and
according to some general rules. These tests cannot verify that the contents
are correct.

In order to truly test the parser output, unit testing is needed. This unit
tests for this parser are located in test/unittests. Unit tests provide one way
to test each parseable quantity and python has a very good [library for unit
testing](https://docs.python.org/2/library/unittest.html).  When the parser
supports a new quantity it is quite fast to create unit tests for it. These
tests will validate the parsing, and also easily detect bugs that may rise when
the code is modified in the future.

## Profiling
The parsers have to be reasonably fast. For some codes there is already
significant amount of data in the NoMaD repository and the time taken to parse
it will depend on the performance of the parser. Also each time the parser
evolves after system deployment, the existing data may have to be reparsed at
least partially.

By profiling what functions take the most computational time and memory during
parsing you can identify the bottlenecks in the parser. There are already
existing profiling tools such as
[cProfile](https://docs.python.org/2/library/profile.html#module-cProfile)
which you can plug into your scripts very easily.

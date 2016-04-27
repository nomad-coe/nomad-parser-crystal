"""
This is a setup script for installing the parser locally on python path with
all the required dependencies. Used to setup the parser locally.
"""
from setuptools import setup


#===============================================================================
def main():
    # Start package setup
    setup(
        name="crystalparser",
        version="0.1",
        description="NoMaD parser implementation for Crystal",
        author="Lauri Himanen",
        author_email="lauri.himanen@gmail.com",
        license="GPL3",
        packages=["crystalparser"],
        install_requires=[
            'pint',
            'numpy',
        ],
        zip_safe=False
    )

# Run main function by default
if __name__ == "__main__":
    main()

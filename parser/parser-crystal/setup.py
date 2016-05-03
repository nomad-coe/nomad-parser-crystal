"""
This is a setup script for installing the parser locally on python path with
all the required dependencies. Used mainly for local testing.
"""
from setuptools import setup, find_packages


#===============================================================================
def main():
    # Start package setup
    setup(
        name="crystalparser",
        version="0.1",
        include_package_data=True,
        package_data={
            'crystalparser.versions.14_103': ['input_data/*.json', 'input_data/*.pickle'],
        },
        description="NoMaD parser implementation for CRYSTAL",
        author="Sami Kivisto",
        author_email="sami.k.kivisto@aalto.fi",
        license="GPL3",
        packages=find_packages(),
        install_requires=[
            'pint',
            'numpy',
        ],
        zip_safe=False
    )

# Run main function by default
if __name__ == "__main__":
    main()

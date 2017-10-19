from setuptools import setup, find_packages


def main():
    setup(
        name="crystalparser",
        version="0.1",
        description="NOMAD parser implementation for Crystal.",
        author="Lauri Himanen",
        author_email="lauri.himanen@aalto.fi",
        license="GPL3",
        package_dir={'': 'parser/parser-crystal'},
        packages=find_packages(),
        install_requires=[
            'nomadcore',
        ],
    )

if __name__ == "__main__":
    main()

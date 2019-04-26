import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="n2yo",
    version="0.0.5",
    author="David Schuster",
    author_email="David.Schuster@gmail.com",
    description="Python wrapper for the N2YO API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/circuitqed/n2yo",
    packages=setuptools.find_packages(),
    install_requires=['requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
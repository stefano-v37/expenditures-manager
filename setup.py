import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ExpendituresManager",
    version="0.0.1",
    author="Stefano Vanin",
    description="Python expenditures manager",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/stefano-v37/expenditures-manager",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
import setuptools

with open("README.md") as fp:
    long_description = fp.read()

setuptools.setup(
    name="PA036 Json Processing",
    description="Performance of JSON processing in MongoDB and PostgreSQL databases",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Martin Balucha, Pavol Pluta, Marko Jovic, Martin Sisak",
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",
        "Typing :: Typed"
    ]
)
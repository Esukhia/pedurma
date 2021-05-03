import re
import setuptools
from pathlib import Path

with open("README.md", "r") as fh:
    long_description = fh.read()

def get_version(prop, project):
    project = Path(__file__).parent / project / "__init__.py"
    result = re.search(
        r'{}\s*=\s*[\'"]([^\'"]*)[\'"]'.format(prop), project.read_text()
    )
    return result.group(1)


setuptools.setup(
    name="pedurma",  # Replace with your own username
    version=get_version("__version__", "pedurma"),
    author="Ngawang Thrinley, Tenzin, Tenzin Kaldan",
    author_email="esukhiadev@gmail.com",
    description="Pedurma Reconstruction functionalities",
    py_modules=["pedurma"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="Apache2",
    url="https://github.com/Esukhia/pedurma",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "antx>=0.1.8, <1.0",
        "openpecha>=0.7.31, <1.0",
    ],
    python_requires=">=3.6",
    tests_require=["pytest"],
)

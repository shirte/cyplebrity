from setuptools import find_packages, setup

# some RDKit versions are not recognized by setuptools
# -> check if RDKit is installed by attempting to import it
# -> if RDKit can be imported, do not add it to install_requires
rdkit_installed = False
try:
    import rdkit

    rdkit_installed = True
except ImportError:
    pass

# rdkit 2022.3.3 is the oldest (reasonable) version
rdkit_requirement = ["rdkit>=2022.3.3"] if not rdkit_installed else []


setup(
    name="cyplebrity",
    version="0.1.1",
    maintainer="Johannes Kirchmair",
    maintainer_email="johannes.kirchmair@univie.ac.at",
    packages=find_packages(),
    url="https://github.com/molinfo-vienna/cyplebrity",
    long_description=open("README.md").read(),
    install_requires=rdkit_requirement
    + [
        "scikit_learn==0.21.2",
        "pandas~=1.2.1",
        "numpy==1.19.2",
        "scipy==1.5.2",
        "molvs==0.1.1",
        "nerdd-module>=0.1.10",
        "fpsim2==0.4.0",
        # avoid warnings about numpy.distutils
        "setuptools < 60.0",
        # install importlib-resources and importlib-metadata for old Python versions
        "importlib-resources>=5; python_version<'3.9'",
        "importlib-metadata>=4.6; python_version<'3.10'",
    ],
    extras_require={
        "dev": [
            "mypy",
            "isort",
            "black",
        ],
        "test": [
            "pytest",
            "pytest-watch",
            "pytest-cov",
            "pytest-bdd",
            "hypothesis",
            "hypothesis-rdkit",
        ],
    },
)
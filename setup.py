from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)-> List[str]:

    '''
    This function returns the list of requirements
    '''

    requirements = []

    with open(file_path) as f:
       requirements = f.readlines()

    requirements = [x.strip("\n") for x in requirements if "-e" not in x]

    return requirements

setup(
    name="MlOpsProject",
    version='0.0.1',
    author='Suraj Desai',
    author_email='surajdesai1297@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements("./requirements.txt")
)
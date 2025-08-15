'''
1.Ths setup.py file is an essential part of packaging and distributing python project.
2.It is used by setuptools to define the configuration of your project, such as its metadata,dependencies, and more.
3.Basically, if your Python project is a product, setup.py is the box label and instruction manual.
4.It helps you organize your MLCode into packages
5.Makes your code reusable,shareable and easier to run on other machine 
'''
'''
Here are the main uses of setup.py in simple terms:

1.Install your project

    ->Lets people run pip install . to put your code on their computer.

2.Share your project

    ->Makes it easy to upload your project to PyPI (Python Package Index) so others can download it with pip install yourpackage.

3.List requirements

    ->Specifies what other Python packages your project needs to work.

4.Add project info

    ->Stores details like version, author, description, and license.

5.Create installable files

    ->Helps generate .whl or .tar.gz files for distribution
'''

'''
Use the find_packages tool from setuptools to automatically look through my project folders and find all the Python packages (folders with __init__.py) so I don’t have to list them by hand
'''
from setuptools import find_packages,setup
from typing import List
def get_requirements() -> List[str]:
    """This function will return List of requirements."""
    requirement_list = []
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                # Ignore empty lines and '-e .'
                if requirement and requirement != '-e .': # # It means only the missing packages are installed, and the whole project doesn’t need to be reinstalled each time.
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print('requirements.txt file not found.')
    return requirement_list
setup(
    name="network_security",
    version='0.0.1',
    author="rithwik",
    author_email="rithwikvasa@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
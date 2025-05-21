from setuptools import find_packages, setup
from typing import List

def get_requirments() -> List[str]:
    requirement_lst: List[str] = []
    try:
        with open('requirments.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e .':  # ✅ fixed typo: requirments → requirement
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirments.txt file not found")

    return requirement_lst

print(get_requirments())

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='chaitanya',
    author_email='chaitanyaprasadkulkarni4@gmail.com',
    packages=find_packages(),
    install_requires=get_requirments()
)

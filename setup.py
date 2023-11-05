""""

# if somebody else wants to install my package in their project then ->
from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='sunny savita',
    author_email='sunny.savita@ineuron.ai',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)

"""

# If i want to install my local package 

from setuptools import find_packages,setup

setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='Pushpakant Shinde',
    author_email='pushpakantshinde@gmail.com',
    #install_requires=["scikit-learn","pandas","numpy"],
    packages=find_packages()
)

from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return list of requirments
    '''

    requirements = []
    with open(file_path) as fileobj:
        requirements = fileobj.readlines()
        requirements = [req.replace('\n','') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='ml_project',
    version='0.0.1',
    author='Deepthi',
    author_email='deepthi.poduri@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')

)
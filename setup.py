from setuptools import find_packages,setup
from typing import List

FILE_NAME='requirements.txt'
HYPHEN_E_DOT='-e .'

def get_requirements(FILE_NAME)->List[str]:
    try:
        with open(FILE_NAME,'r') as f:
            packages=f.readlines()
        
        packages=[i.replace("\n","") for i in packages]
        
        if HYPHEN_E_DOT in packages:
            packages.remove(HYPHEN_E_DOT)


        return packages
       
    except Exception as e:
        raise(e)

setup( 
    name='Insurance', 
    version='0.0.1', 
    description='A project to estimate the insurance premium', 
    author='Pritam Kumar', 
    author_email='singhpritam983@gmail.com', 
    packages=find_packages(), 
    install_requires=get_requirements(FILE_NAME)
) 
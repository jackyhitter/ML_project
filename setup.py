from setuptools import setup, find_packages

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> list:
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        requirements = [req for req in requirements if req != HYPHEN_E_DOT]
    return requirements

setup(
    name='my_package',
    version='0.0.1',
    author='AN',
    author_email = "anunaynaman.bt24civil@pec.edu.in",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

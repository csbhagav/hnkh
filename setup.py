"""setup.py file for packaging ``alexq``."""

from setuptools import setup, find_packages


# read in the readme
with open('readme.md', 'r') as readme_file:
    readme = readme_file.read()


# read in the requirements
with open('requirements.txt', 'r') as requirements_file:
    requirements = [
        ln.strip()
        for ln in requirements_file.split('\n')
    ]


setup(
    name='hnkh',
    version='0.0.1',
    description="HNKH Repository",
    long_description=readme,
    url='http://github.com/csbhagav/hnkh',
    author='Chandra B',
    license='',
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.6',
    scripts=[],
    zip_safe=False
)
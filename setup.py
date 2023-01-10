from os.path import abspath, dirname, join
from setuptools import setup, find_packages

CURDIR = dirname(abspath(__file__))

with open(join(CURDIR, 'requirements.txt'), encoding="utf8") as f:
    REQUIREMENTS = f.read().splitlines()

setup(
    name = 'robotframework-aegis',
    version = '1.0.0',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = REQUIREMENTS,
)
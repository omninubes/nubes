from setuptools import setup, find_packages

setup(
    name='nubes',
    version='0.0.1',
    packages=find_packages(exclude=('tests',)),
    install_requires=['openstacksdk>=0.9.2'],
    entry_points={
        'console_scripts': ['nubes=nubes.cmd:main']
    }
)

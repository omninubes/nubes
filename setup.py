from setuptools import setup

setup(
    name='nubes',
    version='0.0.1',
    packages=['nubes', 'nubes.cmd'],
    url='',
    license='',
    author='',
    author_email='',
    description='',
    install_requires=['openstacksdk>=0.9.2'],
    entry_points={
        'console_scripts': ['nubes=nubes.cmd:main']
    }
)

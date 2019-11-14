from setuptools import setup, find_packages

setup(
    name='besc',
    version='1.0.1',
    packages=find_packages(),
    license='MIT License',
    description='Send data to the ESS API BESC',
    url='https://github.com/rock98rock/BESC-ESS-API-DEV',
    install_requires=['query_string'],
    author='Clive Lim'
)

from setuptools import setup

setup(
    name = 'norman',
    version = '0.1.0',
    packages = ['norman'],
    entry_points = {
        'console_scripts': [
            'normal = norman.__main__:main'
        ]
    })
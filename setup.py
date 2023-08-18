from setuptools import setup

setup(
    name='hchmod',
    version='1.0',
    py_modules=['hchmod'],
    entry_points={
        'console_scripts': [
            'hchmod = hchmod:main'
        ],
    },
)

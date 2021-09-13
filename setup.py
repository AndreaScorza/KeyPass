from setuptools import setup, find_packages

setup(
    name='KeyPass',
    extras_require=dict(tests=['pytest']),
    packages=find_packages(),
    py_modules=['keyPass']
)

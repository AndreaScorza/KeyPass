from setuptools import setup, find_packages

setup(
    name='KeyPass',
    extras_require=dict(tests=['pytest']),
    package=find_packages(where='src'),
    package_dir={"":"src"},
)

# read the contents of your README file
from pathlib import Path

from setuptools import find_packages, setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='featureguards',
    version='0.1.4',
    description='Official Python SDK for FeatureGuards',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/featureguards/featureguards-py',
    author='Bashar Al-Rawi',
    author_email='eng@featureguards.com',
    license='MIT',
    packages=find_packages(),
    install_requires=['grpcio', 'grpcio-status', 'xxhash', 'protobuf'],
    classifiers=[],
)

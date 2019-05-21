
from setuptools import setup, find_packages

setup(
    name='pyUnitTestingExamples',
    version='0.0.1',
    description='Visualization of different testing examples',
    author='Yangyang li',
    author_email='yangyangli@uma.es',
    maintainer='Yangyang li',
    maintainer_email='yangyangli@uma.es',
    license='MIT',
    url='https://github.com/yangly619/pyUnitTestingExamples.git',
    long_description=open('README.md').read(),
    packages=find_packages(exclude=["test.*", "tests"]),
    python_requires='>=3',
    classifiers=[
        'Development Status :: Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering :: Class Exercise',
        'Programming Language :: Python :: 3.7'
    ],
    install_requires=[
        'mockito',
        'unittest'
    ]
)
from setuptools import setup

readme = open('README.rst').read()

setup(
    name='monzo-api-stub',
    version='0.0.1',
    description="Stub API for Monzo",
    long_description=readme,
    author="Dan Palmer",
    author_email='dan@danpalmer.me',
    license='MIT',
    url='https://github.com/danpalmer/monzo-api-stub',
    packages=[
        'monzoapistub',
    ],
    install_requires=[
        'click>=6.6',
        'flask>=0.11',
        'fake-factory>=0.6.0',
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
    ],
    entry_points={
        'console_scripts': [
            'monzo-api = monzoapistub.cli:cli',
        ],
    },
)

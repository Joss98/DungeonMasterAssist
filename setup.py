from setuptools import setup, find_packages
import os

# Read the long description from README.md
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="DungeonMasterAssist",
    version='1.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click>=8.1.7,<9.0.0',
        'prompt_toolkit>=3.0.0,<4.0.0',
        # Other dependencies if any
    ],
    entry_points={
        'console_scripts': [
            'dma = DungeonMasterAssist.cli:main',
        ],
    },
    license='MIT',
    description='A command-line assistant for D&D 5e Dungeon Masters.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/joss98/DungeonMasterAssist',
    author='Josiah Della Foresta',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Games/Entertainment :: Role-Playing',
    ],
    python_requires='>=3.6',
)
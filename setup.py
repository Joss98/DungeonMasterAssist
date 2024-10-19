from setuptools import setup, find_packages

setup(
    name="DungeonMasterAssist",
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        # Other dependencies
    ],
    entry_points={
        'console_scripts': [
            'dma = DungeonMasterAssist.cli:main',
        ],
    },
    license='MIT',
    description='A command-line assistant for Dungeon Masters in D&D 5e.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/joss98/DungeonMasterAssist',
    author='Josiah Della Foresta',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.13',
)
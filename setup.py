from setuptools import Command, find_packages, setup

from src import __version__

setup(
    name = 'shellnerd',
    version = __version__,
    description = 'A CLI to nerd your way through everday shell commands.',
    url = 'https://github.com/aki21j/see-al-i',
    author = 'Ankit Gupta',
    author_email = 'ankitgupta21j@gmail.com',
    license = 'UNLICENSE',
    classifiers = [
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: Public Domain',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords = 'cli',
    packages = find_packages(exclude=['docs', 'tests*']),
    install_requires = [
        # 'PyInquirer',
        # 'elevate',
        # 'ssh-config-json'
    ],
    extras_require = {
        'test': ['coverage', 'pytest', 'pytest-cov'],
    },
    entry_points = {
        'console_scripts': [
            'shellnerd=src.cli:main',
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
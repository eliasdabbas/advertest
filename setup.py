#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'pandas'
]

setup_requirements = [
    'pytest-runner', 
]

test_requirements = [
    'pytest', 
]

setup(
    author="Elias Dabbas",
    author_email='eliasdabbas@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Productivity and analysis tools for online marketing",
    entry_points={
        'console_scripts': [
            'advertest=advertest.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='advertising marketing search-engine-optimization adwords '
             'seo sem bingads keyword-research',
    name='advertest',
    packages=find_packages(include=['advertest']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/eliasdabbas/advertest',
    version='1.0.1',
    zip_safe=False,
)

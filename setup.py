from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.1.0'
DESCRIPTION = 'Make Python console logs look colorful and beautiful!'
LONG_DESCRIPTION = 'Colorized is a Python package that allows you to colorize your Python console logs, even with bold and underline!'

# Setting up
setup(
    name = "colorized",
    version = VERSION,
    author = "KingPr0o7 (Nathan Parker)",
    author_email = "<nathan@ncp.dev>",
    description = DESCRIPTION,
    long_description_content_type = "text/markdown",
    long_description = LONG_DESCRIPTION,
    packages = find_packages(),
    install_requires = [],
    keywords = ['python', 'console', 'color', 'text-formatting'],
    classifiers = [
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
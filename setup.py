import os

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


osname = os.uname()[0]

def readme():
    with open('README.rst') as f:
        return f.read()

if osname == "Linux":
    config = {
        'description': 'PTB Tokenization',
        'long_description': readme(),
        'author': 'murhaff',
        'url': 'https://github.com/Murhaf/toko',
        'download_url': 'https://github.com/Murhaf/toko',
        'author_email': 'murhaff@ifi.uio.no',
        'version': '0.1.0',
        #'install_requires': ['argparse'],
        'packages': find_packages(),
        'scripts': ['bin/tokenize.py'],
        'name': 'toko'
        #entry_points = {
        #    'console_scripts': ['funniest-joke=funniest.command_line:main'],
        #    }
        }


setup(**config)

import os

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


osname = os.uname()[0]

if osname == "Linux":
    config = {
        'description': 'PTB Tokenization',
        'author': 'murhaff',
        'url': 'https://github.com/Murhaf/toko',
        'download_url': 'https://github.com/Murhaf/toko',
        'author_email': 'murhaff@ifi.uio.no',
        'version': '0.1.0',
        #'install_requires': ['argparse'],
        'packages': find_packages(),
        'scripts': [],
        'name': 'toko'
        }


setup(**config)

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'PTB Tokenization',
    'author': 'murhaff',
    'url': 'https://github.com/Murhaf/toko',
    'download_url': 'https://github.com/Murhaf/toko',
    'author_email': 'murhaff@ifi.uio.no',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'toko'
}

setup(**config)

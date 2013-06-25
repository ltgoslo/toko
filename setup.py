import subprocess
from subprocess import call, Popen
import inspect

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
#'install_requires': ['argparse'],
    'packages': ['argparse'],
    'scripts': [],
    'name': 'toko'
}

setup(**config)

wapiti_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + '/bin/wapiti-1.4.0/'
args = ['make']
subprocess.Popen(args,cwd=wapiti_dir)
print wapiti_dir

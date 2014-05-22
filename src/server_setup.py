import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='ReCoRVVA_server',
      version='2.0',
      py_modules=['main','comms','motors','sensors','dhtreader','cam','startstream','install_termcolor','startup'],
      description='ReCoRVVA connection API and wrapper for Python',
      author='F. Anderson, B. James',
      author_email='finnian@fxapi.co.uk, benji@fxapi.co.uk',
      url='http://www.github.com/xavbabe/ReCoRVVA',
      long_description=read('README'),
      )

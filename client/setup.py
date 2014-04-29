import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='ReCoRVVA_client',
      version='1.0',
      py_modules=['recorvva','wiimote','xbox','install_termcolor'],
      description='ReCoRVVA connection API and wrapper for Python',
      author='F. Anderson, B. James, A. Ledesma',
      author_email='finnian@fxapi.co.uk, benji@fxapi.co.uk, monkeeyman@hotmail.co.uk',
      url='http://www.github.com/xavbabe/ReCoRVVA',
      long_description=read('README'),
      )

from setuptools import setup
import sys

from flatdict import __version__

tests_require = ['nose']
if sys.version_info < (2, 7, 0):
    tests_require.append('unittest2')

classifiers = ['Development Status :: 5 - Production/Stable',
               'Intended Audience :: Developers',
               'License :: OSI Approved :: BSD License',
               'Operating System :: POSIX',
               'Programming Language :: Python',
               'Programming Language :: Python :: 2',
               'Programming Language :: Python :: 3',
               'Programming Language :: Python :: 2.6',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3.2',
               'Programming Language :: Python :: 3.3',
               'Programming Language :: Python :: 3.4',
               'Programming Language :: Python :: Implementation :: CPython',
               'Programming Language :: Python :: Implementation :: PyPy',
               'Topic :: Software Development :: Libraries']

setup(name='flatdict',
      version=__version__,
      description=('Python module for interacting with nested dicts as a '
                   'single level dict with delimited keys.'),
      long_description=open('README.rst').read(),
      author='Gavin M. Roy',
      author_email='gavinmroy@gmail.com',
      url='http://github.com/gmr/flatdict',
      package_data={'': ['LICENSE', 'README.rst']},
      tests_require=tests_require,
      py_modules=['flatdict'],
      license=open('LICENSE').read(),
      classifiers=classifiers,
      zip_safe=True)

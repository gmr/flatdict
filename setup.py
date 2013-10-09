from distutils.core import setup
import sys

tests_require = []
if sys.version_info[0:2] == (2,6):
      test_require = ['unittest2']

setup(name='flatdict',
      version='1.1.1',
      description=('Python module for interacting with nested dicts as a '
                   'single level dict with delimited keys.'),
      author='Gavin M. Roy',
      author_email='gmr@meetme.com',
      license='BSD',
      url='http://github.com/gmr/flatdict',
      tests_require=tests_require,
      py_modules=['flatdict'],
      classifiers=['Development Status :: 4 - Beta',
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
                   'Programming Language :: Python :: Implementation :: CPython',
                   'Programming Language :: Python :: Implementation :: PyPy',
                   'Topic :: Software Development :: Libraries'])

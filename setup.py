from setuptools import setup

setup(name='flatdict',
      version='1.1.0',
      description=("Python module for interacting with nested dicts as a "
                   "single level dict with delimited keys."),
      author="Gavin M. Roy",
      author_email="gmr@meetme.com",
      license='BSD',
      url="http://github.com/gmr/flatdict",
      tests_require=['mock'],
      py_modules=['flatdict'],
      classifiers=['Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: POSIX',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7',
                   'Topic :: Software Development :: Libraries'])

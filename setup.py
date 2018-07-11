import setuptools

from flatdict import __version__

setuptools.setup(
    name='flatdict',
    version=__version__,
    description=('Python module for interacting with nested dicts as a '
                 'single level dict with delimited keys.'),
    long_description=open('README.rst').read(),
    author='Gavin M. Roy',
    author_email='gavinmroy@gmail.com',
    url='https://github.com/gmr/flatdict',
    package_data={'': ['LICENSE', 'README.rst']},
    py_modules=['flatdict'],
    license='BSD',
    classifiers=[
        'Topic :: Software Development :: Libraries',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    zip_safe=True)

import setuptools

from flatdict import __version__


def read_requirements(filename):
    requirements = []
    try:
        with open(filename) as req_file:
            for line in req_file:
                if '#' in line:
                    line = line[:line.index('#')]
                line = line.strip()
                if line.startswith('-r'):
                    requirements.extend(read_requirements(line[2:].strip()))
                elif line:
                    requirements.append(line)
    except IOError:
        pass
    return requirements


classifiers = ['Development Status :: 5 - Production/Stable',
               'Intended Audience :: Developers',
               'License :: OSI Approved :: BSD License',
               'Operating System :: POSIX',
               'Programming Language :: Python',
               'Programming Language :: Python :: 2',
               'Programming Language :: Python :: 3',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3.4',
               'Programming Language :: Python :: 3.5',
               'Programming Language :: Python :: 3.6',
               'Programming Language :: Python :: Implementation :: CPython',
               'Programming Language :: Python :: Implementation :: PyPy',
               'Topic :: Software Development :: Libraries']

setuptools.setup(
    name='flatdict',
    version=__version__,
    description=('Python module for interacting with nested dicts as a '
                 'single level dict with delimited keys.'),
    long_description=open('README.rst').read(),
    author='Gavin M. Roy',
    author_email='gavinmroy@gmail.com',
    url='http://github.com/gmr/flatdict',
    package_data={'': ['LICENSE', 'README.rst']},
    tests_require=read_requirements('test-requirements.txt'),
    py_modules=['flatdict'],
    license=open('LICENSE').read(),
    classifiers=classifiers,
    zip_safe=True)

import pkg_resources
import setuptools

setuptools_version = pkg_resources.parse_version(setuptools.__version__)
if setuptools_version < pkg_resources.parse_version('39.2'):
    raise SystemExit('Please upgrade setuptools')
setuptools.setup()

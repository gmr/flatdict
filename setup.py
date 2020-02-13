import pkg_resources
import setuptools

setuptools_version = pkg_resources.parse_version(setuptools.__version__)
if setuptools_version < pkg_resources.parse_version('39.2'):
    raise SystemExit('setuptools 39.2 or greater required for installation')
setuptools.setup()

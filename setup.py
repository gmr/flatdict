import setuptools

try:
    # Try pkg_resources first for backward compatibility
    import pkg_resources
    setuptools_version = pkg_resources.parse_version(setuptools.__version__)
    min_version = pkg_resources.parse_version('39.2')
except (ImportError, ModuleNotFoundError):
    # Fall back to packaging.version if pkg_resources is not available (Python 3.12+)
    from packaging.version import Version
    setuptools_version = Version(setuptools.__version__)
    min_version = Version('39.2')

if setuptools_version < min_version:
    raise SystemExit('setuptools 39.2 or greater required for installation')

setuptools.setup()

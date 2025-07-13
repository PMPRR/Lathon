_packages = []


def add_package(package: str):
    """
    Adds a package to a list of used packages
    """
    _packages.append(package)
    return


def get_packages():
    """
    Return as list of names of all packages currently used on the document
    """
    return _packages

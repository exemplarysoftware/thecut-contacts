from setuptools import setup, find_packages
from version import get_git_version


setup(
    name='thecut-contacts',
    author='The Cut',
    author_email='development@thecut.net.au',
    url='http://projects.thecut.net.au/projects/thecut-contacts',
    namespace_packages=['thecut'],
    version=get_git_version(),
    packages=find_packages(),
    include_package_data=True,
    install_requires=['django-countries>=1.5,<2.0',
                      'django-model-utils>=2.2', 'django-taggit>=0.12.2'],
    )

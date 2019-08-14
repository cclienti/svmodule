from setuptools import setup
from svmodule import __version__


setup(name='svmodule',
      version=__version__,
      description='[System]Verilog Module I/O parser and printer',
      url='https://github.com/cclienti/svmodule',
      author='Christophe Clienti',
      author_email='cclienti@wavecruncher.net',
      license='GPL-3.0',
      packages=['svmodule'],
      install_requires=[],
      entry_points = {'console_scripts': ['svmodp=svmodule.cli:main'],},
      zip_safe=False)

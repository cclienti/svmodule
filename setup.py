from setuptools import setup
from svmodule import __version__


setup(name='svmodule',
      version=__version__,
      description='[System]Verilog Module I/O parser and printer',
      url='https://github.com/cclienti/svmodule',
      author='Christophe Clienti',
      author_email='cclienti@wavecruncher.net',
      license='GPL-3.0',
      packages=['svmodule', 'svmodule.printers'],
      install_requires=[],
      entry_points = {'console_scripts': ['svmodp=svmodule.cli:main'],},
      zip_safe=False
      classifiers=["Programming Language :: Python :: 3",
                   "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
                   "Operating System :: OS Independent",
                   "Development Status :: 5 - Production/Stable",
                   "Environment :: Console",
                   "Intended Audience :: Developers"])

# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    import pypandoc
    LDESC = open('README.md', 'r').read()
    LDESC = pypandoc.convert(LDESC, 'rst', format='md')
except (ImportError, IOError, RuntimeError) as e:
    print("Could not create long description:")
    print(str(e))
    LDESC = ''

setup(name='suflex_zebra',
      version='0.1',
      description='Python package to talk to Zebra label printers, working only on company environment',
      long_description=LDESC,
      author='Alfredo Neto',
      author_email='alfredo@suflex.co',
      url='',
      license='GPL',
      packages=['suflex_zebra'],
      entry_points={
          'console_scripts': [
              'suflex_zebra = suflex_zebra.cli:cli',
          ],
      },
      include_package_data=False,
      zip_safe=True,
      platforms='any',
      install_requires=[
          "click",
          "zpl",
          "Pillow"
      ],
      keywords='Suflex Zebra',
      classifiers=[
          'Development Status :: 1 - Beta',
          'Operating System :: OS Linux',
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
          'Programming Language :: Python :: 3',
          'Topic :: System :: Hardware :: Hardware Drivers',
      ]
)
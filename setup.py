try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

import sys, os

version = '1.0'

setup(name='agenda',
      version=version,
      description="",
      long_description="",
      classifiers=[],
      keywords='',
      author='Mathieu Leduc-Hamel',
      author_email="marrakis@gmail.com",
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      namespace_packages=['agenda',],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'vobject',
        'werkzeug',
        'djangorecipe',
        'django'],
      entry_points={
        'django.apps': [
            'agenda = agenda'
            ],
        'console_scripts':[
            'debug = agenda.command:debug'
            ],
        },
)

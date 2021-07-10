#!/usr/bin/env python

from distutils.core import setup

setup(name='Weather Display',
      packages=['weather_display'],
      include_package_data=True,
      version='0.1',
      description='App for collecting weather event data and serving a web UI',
      author='Stephen De Vight',
      url='https://github.com/devights/weather_display',
      install_requires=[
            'Django==3.2.5',
            'djangorestframework==3.12.2',
            'django-webpack-loader<1.0',

      ]
     )

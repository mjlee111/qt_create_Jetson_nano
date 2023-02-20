#!/usr/bin/env pyyhon

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
      packages=['qt_create'],
      package_dir = {'':'src'},
      scripts = ["scripts/catkin_create_qt_pkg"],
      package_data = {'qt_create': [
           'templates/CATKIN_IGNORE',
           'templates/qtros/CMakeLists.txt',
           'templates/qtros/src/*.cpp',
           'templates/qtros/src/*.ui',
           'templates/qtros/include/PACKAGE_NAME/*.h',
           'templates/qtros/resources/*.qrc',
           'templates/qtros/resources/images/*.jpg',
           'templates/qtros/package.xml',
           ]},
      requires=[]
      )

setup(**d)


# qt_create

## This package is for making QT based GUI ROS package in terminal.

## Because ARM PC's can't install qt_ros_plugin, you can use this package to make fully fuctional QT ROS package.

### Enter 
```
$ catkin_create_qt_pkg [package name] [dependencies]
```

#### The created package already includes std_msgs and roscpp so you don't have to add it. 

# Create.py
```python
import os
import shutil
from utils import author_name
from utils import read_template
from utils import instantiate_template

##############################################################################
# Template
##############################################################################

def get_qt_text_templates(package, type):
    template_dir = os.path.join(os.path.dirname(__file__),'templates',type) 
    templates = {}
    templates['CMakeLists.txt'] = read_template(os.path.join(template_dir,'CMakeLists.txt'))
    templates['package.xml'] = read_template(os.path.join(template_dir,'package.xml'))
    templates[os.path.join('src','mainwindow.ui')] = read_template(os.path.join(template_dir,'src','mainwindow.ui'))
    templates[os.path.join('src','main.cpp')] = read_template(os.path.join(template_dir,'src','main.cpp'))
    templates[os.path.join('src','mainwindow.cpp')] = read_template(os.path.join(template_dir,'src','mainwindow.cpp'))
    templates[os.path.join('resources','images.qrc')] = read_template(os.path.join(template_dir,'resources','images.qrc'))
    templates[os.path.join('include',package,'mainwindow.h')] = read_template(os.path.join(template_dir,'include','PACKAGE_NAME','mainwindow.h'))
    return templates

def create_qt_ros_package(package, depends, type):
    
    p = os.path.abspath(package)
    os.makedirs(os.path.join(p,"src"))
    os.makedirs(os.path.join(p,"include"))
    os.makedirs(os.path.join(p,"include",package))
    os.makedirs(os.path.join(p,"resources"))
    os.makedirs(os.path.join(p,"resources","images"))
    print "Created qt package directories."

    # Qt text files
    templates = get_qt_text_templates(package, type)
    for filename, template in templates.iteritems():
        contents = instantiate_template(template, package, package, author_name(), depends)
        try:
            p = os.path.abspath(os.path.join(package, filename))
            f = open(p, 'w')
            f.write(contents)
            print "Created package file", p
        finally:
            f.close()
    # Qt binary files
    template_dir = os.path.join(os.path.dirname(__file__),'templates',type) 
    shutil.copy(os.path.join(template_dir,'resources','images','icon.jpg'),
                os.path.join(os.path.abspath(package),'resources','images','icon.jpg'))
    
def create_qt_ros_catkin_package(package, depends):
    create_qt_ros_package(package, depends, 'qtros')
```

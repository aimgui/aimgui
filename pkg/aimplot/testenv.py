from distutils.sysconfig import get_python_inc
print(get_python_inc())
import distutils.sysconfig as sysconfig 
print(sysconfig.get_config_var('LIBDIR'))
import os
print(os.environ['VIRTUAL_ENV'])
import os
import sys
from optparse import OptionParser

parser = OptionParser()
parser.add_option('-i', '--init',
  dest='init',
  help='Directory')
parser.add_option('-b', '--buildsystem',
  dest='buildsystem',
  help='Build system (cmake,gyp,unix makefiles)')
parser.add_option('-t', '--tests',
  dest='tests',
  action='store_true',
  help='Enable unit tests')
(option, args) = parser.parse_args()
print option,option
if option.init is not None:
  if os.path.isdir(option.init):
    sys.stderr.write('Directory already exists\n')
    sys.exit(1)
  else:
    # bootstrap project
    os.makedirs(option.init)
    if option.buildsystem == 'cmake':
      with open(os.path.join(option.init, 'CMakeLists.txt'), 'w') as f:
        f.write('cmake_minimum_required (VERSION 2.8.7)\n')
        f.write('project ({0})\n'.format(option.init))
        f.write('\n')
        if option.tests:
          f.write('option (BUILD_TESTS "Build test suite" OFF)\n')
          f.write('\n')
        f.write('add_executable ({}\n'.format(option.init))
        f.write('	src/main.cpp)\n')
        if option.tests:
          f.write('if (BUILD_TESTS)\n')
          f.write('	add_subdirectory (tests)\n')
          f.write('endif ()\n')
      if option.tests:
        os.makedirs(os.path.join(option.init, 'tests'))
        with open(os.path.join(option.init, 'tests', 'CMakeLists.txt'), 'w') as f:
          f.write('# Unit tests\n')
      # Main source
      os.makedirs(os.path.join(option.init, 'src'))
      with open(os.path.join(option.init, 'src', 'main.cpp'), 'w') as f:
        f.write('#include <iostream>\n')
        f.write('\n')
        f.write('int\n')
        f.write('main(int argc, char * argv[])\n')
        f.write('{\n')
        f.write('}\n')

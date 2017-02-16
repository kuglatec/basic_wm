# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#    Copyright (C) 2017 Chuan Ji <ji@chu4n.com>                               #
#                                                                             #
#    Licensed under the Apache License, Version 2.0 (the "License");          #
#    you may not use this file except in compliance with the License.         #
#    You may obtain a copy of the License at                                  #
#                                                                             #
#     http://www.apache.org/licenses/LICENSE-2.0                              #
#                                                                             #
#    Unless required by applicable law or agreed to in writing, software      #
#    distributed under the License is distributed on an "AS IS" BASIS,        #
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. #
#    See the License for the specific language governing permissions and      #
#    limitations under the License.                                           #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import subprocess

def FlagsForFile(filename, **kwargs):
  gtkmm_cflags = subprocess.check_output([
      'pkg-config',
      '--cflags-only-I',
      'gtkmm-3.0',
  ], universal_newlines=True).split()
  return {
      'flags': [
          '-x', 'c++',
          '-std=c++1y',
          '-Wall',
          '-Werror',
      ] + gtkmm_cflags,
  }
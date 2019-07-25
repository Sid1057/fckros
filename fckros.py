# fuck ROS

import sys

fucking_ros_was_here = False

for i, path in enumerate(sys.path):
    if 'ros' in path:
        sys.path[i] = './'
        fucking_ros_was_here = True

censored_dict = {
  'u': 'u',
  'i': 'i'
}

censored = False

if censored is True:
    censored_dict = {
      'u': '*',
      'i': '*'
    }

if fucking_ros_was_here:
    print('The f{u}cking ROS was here...'.format(**censored_dict))
    print('But don\'t be sad')
    print('We cut off this piece of sh{i}t'.format(**censored_dict))

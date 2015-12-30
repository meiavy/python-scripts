import os
import sys

def get_subdir(path_name):
    print "tar subdir for "+path_name
    file_names = os.listdir(path_name)
    for name in file_names:
        if os.path.isdir(name):
            abs_path=os.path.abspath(name)
            command='tar -cvf "'+abs_path+'.tar" "'+ abs_path+'/"';
            print command
            os.system(command)


if len(sys.argv) < 2:
    print "please enter parent dir..."
    exit(1)

if not os.path.isdir(sys.argv[1]):
    print "param must be a dir..."
    exit(1)

get_subdir(sys.argv[1])

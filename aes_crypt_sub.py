import os
import sys
import uuid

def crypt_subdir(path_name,log_file):
    print "crypt subdir for "+path_name
    file_names = os.listdir(path_name)
    for name in file_names:
        if os.path.isfile(name):
            abs_path=os.path.abspath(name)
            _,ext=os.path.splitext(abs_path)
            source=abs_path
            dest=str(abs(hash(uuid.uuid4().get_hex())))+ext+'.aes-128-cbc'
            command='openssl aes-128-cbc -k a19821005 -in "'+source+'" -out "'+ dest+'"';
            print command
            os.system(command)
            log(log_file,os.path.basename(dest)+"\t\t\t"+os.path.basename(source))

def log(log_file,msg):
    logger=open(log_file, "ab+")
    logger.write(msg+"\n")
    logger.close()


if len(sys.argv) < 3:
    print "please enter: parent dir,logpath..."
    exit(1)

if not os.path.isdir(sys.argv[1]):
    print "param must be a dir..."
    exit(1)


crypt_subdir(sys.argv[1],sys.argv[2])

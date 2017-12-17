import os
import shutil

# Check current working directory.
path = os.getcwd()
retval = os.getcwd()
print ("Current working directory %s" % retval)




def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

print (get_size(path))

def copy_functionUSB():
	size = get_size()
	while size > 1000:
		print("hello bitches")
		

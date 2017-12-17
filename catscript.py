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

def freespace(p):
    s = os.statvfs(p)
    return s.f_bsize * s.f_bavail
    


def copy_functionUSB():
	size = freespace(path) - get_size() 
	count = 0
	while size > 1000:
		print(count)
		count = count + 1
		
		

print(freespace(path))

print (get_size(path))

print (freespace(path)-get_size(path))
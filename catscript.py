import ctypes
import os
import platform
import sys
import shutil
import time 



# Check current working directory.
path = os.getcwd()
retval = os.getcwd()
string = "/cat.jpg"
newpath = path+string
print ("Current working directory %s" % path)





def get_free_space_mb(dirname):
    """Return folder/drive free space (in megabytes)."""
    if platform.system() == 'Windows':
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(dirname), None, None, ctypes.pointer(free_bytes))
        return free_bytes.value / 1024 / 1024
    else:
        st = os.statvfs(dirname)
        return st.f_bavail * st.f_frsize / 1024 / 1024
        

def copy_function():
	value = get_free_space_mb(path)
	print ("Current newpath directory %s" % newpath)
	while value > 1000:
		shutil.copy2(newpath, '{}.jpg'.format(i))

	
copy_function()
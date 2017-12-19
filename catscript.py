import ctypes
import os
import platform
import sys
import shutil


# Grab the current directory
path = os.getcwd()
retval = os.getcwd()
string = "/cat.jpg"
newpath = path+string
print ("Current directory %s" % path)


# Check current working directory.
path = os.getcwd()
retval = os.getcwd()
print ("Current working directory %s" % retval)



def free_space(path):		#Determines the free space on the drive. Windows might be inaccurate.
    if platform.system() == 'Windows':
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(path), None, None, ctypes.pointer(free_bytes))
        return free_bytes.value / 1024 / 1024
    else:
        st = os.statvfs(path)
        return st.f_bavail * st.f_frsize / 1024 / 1024

        

def copy_function():	#Perform the copy on the path gathered from getcwd.
#	print ("Current newpath directory %s" % newpath)
	value = free_space(path)
	count = 0
	while value > 100.00: #While available memory is > 100 Mb
		shutil.copy2('cat.jpg', '{}.jpg'.format(count))
		count += 1
		print("Space remaining." + str(free_space(path)))


copy_function()
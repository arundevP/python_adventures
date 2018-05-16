#!/usr/bin/python
import os
import sys
from pprint import pprint

"""
Various Os modules experimented upon
Exception: Os related exceptions raise OSError
site.py: This module 'site' is automatically imported during initialization.
         This automatic import can be suppressed using the interpreter's -s option.
         Constructs up to four directories from a head and tail part.
            >> python -m site --user-site
File Descriptors: FD are small integers corresponding to a file that has been opened
        by the current process. The standard input is usually FD 0, standard output is 1
        and standard error is 2.


Modules :
        1.  name: gives the name of the operating system dependent module.
                    os.name , os.uname(), alternative : sys.platform
        2.  environ : A mapping object representing the string environment.
                    The mapping is captured the first time the os module is imported
                    typically during the python startup as part of processing site.py
                    If the platform supports theputenv() function this mapping may be
                    used to modify the environment as well as query the environment.
                    putenv() will be called automatically  when this mapping is modified.
                    os.environ is another alternative to using putenv() to modify environment.
                    os.environ.clear() , os.environ.pop() .
                    
        3. ctermid: return the filename corresponding to the controlling terminal of the process
        
        4. id's : getegid() - get the effective group ids of the current process.
                  geteuid() -get the effective uid of the current process.
                  getgid() - get the real gid for the current process.
                  getlogin() - get the name of the user logged in on the controlling terminal
                  
        5. os.fdopen(fd[,mode[, bufsize]]) : returns the open file object connected to the file
                            descriptor fd. If the fdopen raises an exception it leaves the fd
                            untouched. ??#FIXMEhow to use
                            
        6. os.tmpfile(): Returns the file descriptor of an temporary file created opend in update
                         mode. (w+b). this file will be deleted when there are no more file
                         descriptors to this file.
                         
        7. os.close(fd): Close the file descriptor fd.
           os.closerange(fd_low, fd_high): Close all the file descriptors from fd_low to fd_high.
           
        8. 
"""
if __name__ == "__main__":
    #os.name
    #pprint (os.name)    #'posix'
    #pprint  (os.uname())   #('Linux', 'akku', '4.15.0-20-generic',\
                           # '#21-Ubuntu SMP Tue Apr 24 06:16:15 UTC 2018', 'x86_64')
    #pprint  (sys.platform) # 'linux2'
    
    #pprint (os.environ)
    """{'MATE_DESKTOP_SESSION_ID': 'this-is-deprecated', 'XDG_GREETER_DATA_DIR':
                        '/var/lib/lightdm-data/arun', 'LESSOPEN': '| /usr/bin/lesspipe %s', 'XDG_SESSION_TYPE': 'x11',
                        'LOGNAME': 'arun', 'USER': 'arun', 'HOME': '/home/arun', 'XDG_VTNR': '7',
                        'PATH': '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin',
                        'DISPLAY': ':0.0', 'SSH_AGENT_PID': '1851', 'LANG': 'en_IN', 'TERM': 'xterm', 'SHELL': '/bin/bash',
                         'XDG_SESSION_PATH': '/org/freedesktop/DisplayManager/Session0', 'XAUTHORITY': '/home/arun/.Xauthority',
                        'LANGUAGE': 'en_US', 'SESSION_MANAGER': 'local/akku:@/tmp/.ICE-unix/1529,unix/akku:/tmp/.ICE-unix/1529',
                        'SHLVL': '1', 'QT_QPA_PLATFORMTHEME': 'gtk2' """
                        
                        
    #print os.environ.pop("LANGUAGE")    # en_us
    #print os.ctermid() # /dev/tty
    #print os.getegid()  # 1000
    #print os.geteuid()  # 1000
    #print os.getgid()   # 1000
    #print os.getlogin() # arun returns the environment LOGNAME value
    
    #File and object functions
    #print os.fdopen(2) ????? #FIXME
    print os.tmpfile()    #<open file '<tmpfile>', mode 'w+b' at 0x7f88dbc1fd20>
    fd = os.tmpfile()
    #print fd.write("arun")
    print fd.fileno()   # 4 the file descriptor goes up incrementally 0, 1,
                        #2 , this script 3 and the opened file des 4
    
    print os.close(fd.fileno()) 
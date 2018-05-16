import subprocess
import os

"""
subprocess module functions

The subprocess modules lets us spawn new processes , connect to their input/
output/error pipe and get their return code.
shell=True or shell=False use case = ?

Modules:
        1. subprocess.call(): Run the command described in the args list.
                              Wait for the command to complete, then return
                              the returncode attribute.
                              Do not use stdout=subprocess.Pipe or such when
                              using subprocess.call , as it may lead to deadlocks.
                              If pipes are needed then use subprocess.Popen()
                              and communicate()
        2.subprocess.check_call(): Run command described in the args list. Wait
                              for the command to complete. If the return code is
                              0 return ; otherwise raise a CalledProcessError.
                              The CalledProcessError will have the returncode value.
        
        
        
"""

if __name__ == "__main__":
    print "Subprocess module Practice"
    print "subprocess.call"
    returncode = subprocess.call(['ls','-la'], stdin=None, stdout=None, stderr=None, shell=False)
    print "returncode", returncode # 0
    print "#"*70
    print "subprocess.check_call"
    returncode2 = subprocess.check_call(['ls','-lht'], stdin=None, stdout=None, stderr=None, shell=False)
    print "returncode 2", returncode2 # 0
    print "#"*70 
    #print "subprocess.check_call"
    #returncode3 = subprocess.check_call(['tar', '1'], stdin=None, stdout=None, stderr=None, shell=True)
    #print "Returncode 3", returncode3 #CalledProcessError: Command '['tar', '1']' returned non-zero exit status 2
    
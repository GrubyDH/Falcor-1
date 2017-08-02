import subprocess
import os
import shutil
import stat


def directoryCleanOrMake(destination) :
    
    # Check if the Directory exists, and make it if it does not.
    if not os.path.isdir(destination):
        try:
            os.makedirs(destination)
        except OSError, info:
            print "Error trying to Create Directory : " + destination

    else:
        try:
            # Create the arguments.
            batchArgs = ["RemoveDirectoryTree.bat ", destination]

            # Clean the Directory.
            removeDirectoryReturnCode = subprocess.call(batchArgs)

            # Check if it was success.            
            if removeDirectoryReturnCode != 0
                print "Error trying to clean Directory : " + destination

        except subprocess.CalledProcessError:
            print "Error trying to clean Directory : " + destination
            


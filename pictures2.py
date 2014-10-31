#!/usr/bin/python
#I have /media/CAMERA with a bunch of *.JPG files in different
#directories.
#
#I have /home/carles/fotos with subdirectories and also *.JPG (from this
#camera, another camera, the phone, friends that sent me pictures, etc.)
#(fotos is the spelling for photos in Catalan -and Spanish)
#
#I usually copy the photos from /media/CAMERA (camera SD card) to
#/home/carles/fotos and in the correct subdirectories (they are always
#something like "2014-03-19 Easter", "2014-05-10 London-Loop-Elstree-MoorPark", eetc. but this is not relevant.
#
#Question: which photos I have in the camera and are not in
#/home/carles/fotos ?
#
#I realized that I had a few photos from a hike that I didn't copy and I
#completely forgot. So I wondered which other photos I forgot.
#

###############################################################################
# Makes assumption that there are only one level of directories under base 
###############################################################################

import os
import re

extensions=[".JPG", ".jpg", ".PNG", ".png"]
sd="/media/camera/dcim/"
home="/media/pictures/"

def build_files_set(rootdir):
    root_to_subtract = re.compile(r'^.*?' + rootdir + r'[\\/]{0,1}')

    # Create an empty tuple for holding filenames
    files_set = set()
    # Construct paths with filenames
    for (dirpath, dirnames, filenames) in os.walk(rootdir):
        for filename in filenames + dirnames:
            # Filter out unwanted extensions
            for extension in extensions:
                if extension in filename:
                    full_path = os.path.join(dirpath, filename)
                    relative_path = root_to_subtract.sub('', full_path, count=1)
                    files_set.add(relative_path)

    return files_set

def compare_directories(sd, home):
    sd_files = build_files_set(sd)
    home_files = build_files_set(home)

    # Check missing files both ways
    return (sd_files - home_files, home_files - sd_files)

if __name__ == '__main__':

    # Call out compare to get differences
    in_sd, in_home = compare_directories(sd, home)

    # Print out results
    print '\nFiles only in {}:'.format(sd)
    for relative_path in in_sd:
        print '* {0}'.format(relative_path)

    print '\nFiles only in {}:'.format(home)
    for relative_path in in_home:
        print '* {0}'.format(relative_path)
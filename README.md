# ArtifactDownloader

What can the script do for us?
    Download all the debug and release libs from jenkins, so we dont have to build it locally

What is downloaded exactly. 
 - all z-wave lib (debug & release)
 - all zpal lib (debug & release)
 - all bootloader (ota & otw)
 - RAIL libraries
 - nvm3 libs

What steps are needed before first run:
 - get python3
 - get cygwin or WSL
 - setup the variable at the top of the python file:

How can I use the script?

The parameters are optional, you can add the target brach of the z-wave stuff, and the target branch of the super too.
The develop/22q4 are the default if no parameter is given

Example call:
```
python3 download_artifacts.py --zbranch develop/22q4 --branch develop/22q4
```
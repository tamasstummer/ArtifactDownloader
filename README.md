# ArtifactDownloader

What can the script do for us?
    Download all release libs from jenkins, so we dont have to build it locally
    Can build debug libs what we don't store

What is downloaded exactly. 
 - all z-wave lib (release)
 - all zpal lib (release)
 - all bootloader (ota & otw)
 - RAIL libraries
 - nvm3 libs

What can be built?
 - all z-wave lib (debug)
 - all zpal lib (debug)

What steps are needed before first run:
 - get python3
 - get MSYS2 with wget and make installed.

## Usage

### Download release libs
```bash
python download_artifacts.py
```
### Download release libs and build debug libs
```bash
python download_artifacts.py --debug
```
### Build debug libs only
```bash
python download_artifacts.py --only_debug
```
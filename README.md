# HowLongToDownload
The script calculates how long it takes to load a file of the specified size at a specified speed.

Change MAX_SPEED on your speed your internet connection

At startup it expects two arguments, the file size in gigabytes, and the connection speed in kilobytes.

Example:
    HowLong.py 3 512
    
Shows you how long a 3 gigabyte file will be downloaded at 512 KB/s speed.

In case of passing only one argument, the script will take the speed from the MAX_SPEED constant.
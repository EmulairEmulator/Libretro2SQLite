# Prerequisites
Make sure you have the latest versions of GCC, Python and Git Bash installed on your computer.

# Usage
### Manual usage on any OS
  - open Git Bash
  - navigate to the current folder (by typing ```cd whatever/path/you/have/Libretro2SQLite```)
  - clone the Libretro databse files in .rdb format (by typing ```git clone https://github.com/libretro/libretro-database```)
  - clone some necessary RetroArch files (by typing ```git clone https://github.com/libretro/RetroArch```)
  - navigate to *RetroArch/libretro-db* (by typing ```cd RetroArch/libretro-db```)
  - build the RetroArch database (by typing ```make```)
  - copy the file *libretrodb_tool.c* to the root folder (by typing ```cp ./libretrodb_tool.c ../..```)
  - go back to the root folder (by typing ```cd ../..```)
  - generate the .sqlite file (by typing ```python3 libretro-sqlite-db.py``` if you placed Python in your *PATH* environment variable or ```py libretro-sqlite-db.py``` if you are using the Python launcher)

### Automatic Usage on Linux
On Linux, open a terminal and simply run the file *ci.sh* and everything will be generated automatically.
  
### Automatic Usage on Windows
On Windows, only the manual way makes sense. The automatic way is not so automatic because it requires a lot of setup, which is why I do not recommend it. However, here is what you need to do:

[COMING SOON]

### Automatic Usage on Mac
Unfortunately, I do not know how any automatic input would work on Mac. Feel free to contribute to this short documentation if you find out.

# Postrequisites
Don't forget to regularly update the *Retroarch* and the *libretro-database* folders by navigating to each of them using Git Bash, then typing ```git pull```.

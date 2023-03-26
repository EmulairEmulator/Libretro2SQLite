## Prerequisites
Make sure you have the latest versions of GCC and Git Bash installed on your computer.

## Usage on Linux
There are two ways in which you can use this tool on Linux: automatically or manually.

#### 1. Automatic input
Simply run the file *ci.sh* and everything will be generated automatically.

#### 2. Manual input
It requires to perform the following actions and input the following commands into Git Bash:
  - open Git Bash
  - navigate to the current folder (type ```cd whatever/path/you/have/Libretro2SQLite```)
  - clone the Libretro databse files in .rdb format (type ```git clone https://github.com/libretro/libretro-database```)
  - clone some necessary RetroArch files (type ```git clone https://github.com/libretro/RetroArch```)
  - navigate to *RetroArch/libretro-db* (type ```cd RetroArch/libretro-db```)
  - build the RetroArch database (type ```make```)
  - copy the file *libretrodb_tool.c* to the root folder (type ```cp ./libretrodb_tool.c ../..```)
  - go back to the root folder (type ```cd ../..```)
  - generate the .sqlite file (type ```py libretro-sqlite-db.py```)

Don't forget to regularly update the *Retroarch* and the *libretro-database* folders.
  
## Usage on Windows
Technically, there are two ways in which you can use this tool on Windows, automatically or manually, however, only the manual way makes sense. The automatic way is not so automatic and requires a lot of setup.

### 1. "Automatic" input
[COMING SOON]

### 2. Manual input
[COMING SOON]

## Usage on Mac
Unfortunately, I do not know how to use this tool on Mac. Feel free to contribute to this short documentation if you find out.

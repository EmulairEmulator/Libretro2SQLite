## Usage on Linux
There are two ways in which you can use this tool on Linux: automatically or manually.

#### 1. Automatic input
Simply run the file *ci.sh* and everything will be generated automatically.

#### 2. Manual input
It requires to perform the following actions and input the following commands into Git Bash (which you need to install first):
  - open Git Bash
  - navigate to the current folder (type ```cd whatever/path/you/have/Libretro2SQLite```)
  - clone the Libretro databse files in .rdb format (type ```git clone https://github.com/libretro/libretro-database```)
  - clone some necessary RetroArch files (type ```git clone https://github.com/libretro/RetroArch```)
  - navigate to *RetroArch/libretro-db* (type ```cd RetroArch/libretro-db```)
  - build the RetroArch database (type ```make```)
  - copy the file *libretrodb_tool.c* to the root folder (type ```cp ./libretrodb_tool ../..```)
  - go back to the root folder (type ```cd ../..```)
  - generate the .sqlite file (type ```python3 libretro-sqlite-db.py```)

Don't forget to regularly update the *Retroarch* and the *libretro-database* folders
  
## Usage on Windows
[COMING SOON]

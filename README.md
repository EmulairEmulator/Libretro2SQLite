# What it does
[COMING SOON]

# Usage
### Prerequisites
Make sure you have the latest versions of GCC, Python and Git Bash installed on your computer.

### Manual usage on any OS
  - open Git Bash
  - navigate to the current folder (by typing ```cd whatever/path/you/have/Libretro2SQLite```)
  - clone the Libretro databse files in .rdb format (by typing ```git clone https://github.com/libretro/libretro-database```)
  - clone some necessary RetroArch files (by typing ```git clone https://github.com/libretro/RetroArch```)
  - navigate to *RetroArch/libretro-db* (by typing ```cd RetroArch/libretro-db```)
  - build the RetroArch database (by typing ```make```)
  - copy the file *libretrodb_tool.c* to the root folder (by typing ```cp ./libretrodb_tool.c ../..```)
  - go back to the root folder (by typing ```cd ../..```)
  - generate the .sqlite file (by typing ```python3 libretro-sqlite-db.py``` if you placed Python in your *PATH* environment variable or ```py libretro-sqlite-db.py``` if you are using the Python launcher instead)

### Automatic usage on Linux
On Linux, open a terminal and simply run the file *automatic-with-python-path.sh* if you placed Python in your *PATH* environment variable or *automatic-with-python-launcher.sh* if you are using the Python launcher instead. After you've done this, simply wait for the process to finish, because everything will be generated automatically.
  
### Automatic usage on Windows
On Windows, the automatic method can be done in two ways:
1. Install the WSL command, open Command Prompt, navigate to this folder (*whatever/path/you/have/Libretro2SQLite*) and type ```bash automatic-with-python-path.sh``` or ```bash automatic-with-python-launcher.sh```, depending on how you installed Python on your machine.
2. Add "Git Bash Here" to your context menu, right click on this folder (*whatever/path/you/have/Libretro2SQLite*), select "Git Bash Here" and type ```sh automatic-with-python-path.sh``` or ```sh automatic-with-python-launcher.sh```, depending on how you installed Python on your machine.

### Automatic usage on Mac
Unfortunately, I don't know how any automatic input would work on Mac. I'm guessing it's similar to the automatic usage on Windows, however, feel free to contribute to this short documentation if you find out exactly how it should be done.

### Postrequisites
Don't forget to regularly update the *Retroarch* and *libretro-database* folders by navigating to each of them using Git Bash, then executing ```git pull```.

# Credits
Major thanks to [Swordfish90](https://github.com/Swordfish90), [konsumer](https://github.com/konsumer) and [rwnobrega](https://github.com/rwnobrega) because this tool is a fork of [libretro-sqlite-db](https://github.com/Swordfish90/libretro-sqlite-db).

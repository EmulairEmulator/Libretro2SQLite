# Usage
### Prerequisites
Make sure you have the latest versions of GCC, Python and Git Bash installed on your computer.

### Manual usage on any OS
  - open Git Bash
  - navigate to the current folder (by typing `cd whatever/path/you/have/Libretro2SQLite`)
  - clone the Libretro databse files in .rdb format (by typing `git clone https://github.com/libretro/libretro-database`)
  - clone some necessary RetroArch files (by typing `git clone https://github.com/libretro/RetroArch`)
  - navigate to *RetroArch/libretro-db* (by typing `cd RetroArch/libretro-db`)
  - build the RetroArch database (by typing `make`)
  - copy the file *libretrodb_tool.c* to the root folder (by typing `cp ./libretrodb_tool.c ../..`)
  - go back to the root folder (by typing `cd ../..`)
  - generate the .sqlite file (by typing `python3 libretro2sqlite.py` if you placed Python in your *PATH* environment variable or `py libretro2sqlite.py` if you are using the Python launcher instead)

### Automatic usage on Linux
On Linux, open a terminal and simply run the file *automatic-with-python-path.sh* if you placed Python in your *PATH* environment variable or *automatic-with-python-launcher.sh* if you are using the Python launcher instead. After you've done this, simply wait for the process to finish, because everything will be generated automatically.
  
### Automatic usage on Windows
On Windows, the automatic method can be done in two ways:
1. Install the WSL command, open Command Prompt, navigate to this folder (*whatever/path/you/have/Libretro2SQLite*) and type `bash automatic-with-python-path.sh` or `bash automatic-with-python-launcher.sh`, depending on how you installed Python on your machine. If you get the error "syntax error: unexpected end of file", [use this tool](https://toolslick.com/conversion/text/dos-to-unix) to convert the files to a compatible format (when uploading those 2 files to GitHub, their special line endings get removed, which is why this error occurs; the tool mentioned above brings them back).
2. Right click this folder (*whatever/path/you/have/Libretro2SQLite*), select "Git Bash Here" ([you can add it](https://stackoverflow.com/questions/24386657/how-to-add-a-open-git-bash-here-context-menu-to-the-windows-explorer) if you don't see it in your context menu) and type `sh automatic-with-python-path.sh` or `sh automatic-with-python-launcher.sh`, depending on how you installed Python on your machine.

### Automatic usage on Mac
Unfortunately, I don't know how any automatic input would work on Mac. I'm guessing it's similar to the automatic usage on Windows, however, feel free to contribute to this short documentation if you find out exactly how it should be done.

### Postrequisites
Don't forget to regularly update the *Retroarch* and *libretro-database* folders by navigating to each of them using Git Bash, then executing `git pull`.
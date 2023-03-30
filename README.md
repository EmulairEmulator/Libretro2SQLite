# Description
This is a small Python script that converts all of RetroArch's .rdb files into a single .sqlite file so it can be used in an emulator front-end such as [Lemuroid](https://github.com/Swordfish90/Lemuroid) or [Emulair](https://github.com/RaduBratan/Emulair).

# Usage on Windows
### Prerequisites
To use this tool on Windows, you will need to install and use MSYS2. To do this, follow those steps:
1. [download the MSYS2 installer](https://www.msys2.org/) from the official website and follow their installation instructions
2. follow [the Libretro Doc's instructions](https://docs.libretro.com/development/retroarch/compilation/windows/) for developing RetroArch on Windows (skip installing Qt and the NVIDIA CG toolkit, stop when you reach the "RetroArch Compilation" section).

Also, it's a good idea to [download Git](https://git-scm.com/download/win), but not necessary.

### Manual usage
- open MSYS2 MINGW64 (for 64-bit computers) or MINGW32 (for 32-bit computers)
- navigate to the current folder by typing `cd whatever/path/you/have/Libretro2SQLite` (mine, for example, is simply *D:/Libretro2SQLite*, but yours could differ depending on where you cloned this repo)
- clone the Libretro databse files in .rdb format by typing `git clone https://github.com/libretro/libretro-database`
- clone some necessary RetroArch files by typing `git clone https://github.com/libretro/RetroArch`
- navigate to *RetroArch/libretro-db* by typing `cd RetroArch/libretro-db`
- build the RetroArch database by typing `make`
- copy the file *libretrodb_tool.exe* to the root folder by typing `cp ./libretrodb_tool ../..`
- go back to the root folder by typing `cd ../..`
- generate the .sqlite file by typing `python3 libretro2sqlite.py`

### Automatic usage
- open MSYS2 MINGW64 (for 64-bit computers) or MINGW32 (for 32-bit computers)
- navigate to the current folder by typing `cd whatever/path/you/have/Libretro2SQLite`
- type `sh automatic-sqlite-generation.sh`

### Error messages
- If you encounter "make: Nothing to be done for 'all'.", simply type `make clean` and start the process again.
- If you get the error "syntax error: unexpected end of file", [use this tool](https://toolslick.com/conversion/text/dos-to-unix) to convert the *.sh* file to a compatible format (when uploaded to GitHub, the special line endings of *automatic-sqlite-generation* get removed, which is why this error occurs; the tool mentioned above brings them back).

### Postrequisites
Don't forget to regularly update the *Retroarch* and *libretro-database* folders by navigating to each of them and executing `git pull`.

# Usage on Linux
I have no idea how much of the "Usage on Windows" section applies here. Feel free to update this documentation if you know the full instructions of using this tool on Linux.

# Usage on macOS
I also have no idea how one would use this tool on macOS. Feel free to update this documentation if you know the full instructions of using this tool on macOS.

# Credits
Major thanks to [Swordfish90](https://github.com/Swordfish90), [konsumer](https://github.com/konsumer) and [rwnobrega](https://github.com/rwnobrega) because this tool is a fork of [libretro-sqlite-db](https://github.com/Swordfish90/libretro-sqlite-db).

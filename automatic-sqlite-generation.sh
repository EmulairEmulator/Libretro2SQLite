#!/bin/bash
#
CWD=`pwd`

build_libretrodb_tool() {
  cd RetroArch/libretro-db
  make clean
  make all
  cp ./libretrodb_tool $CWD
  cd $CWD
}

if [ ! -d libretro-database ];then
  git clone --depth=1 https://github.com/libretro/libretro-database
else
  cd libretro-database
  git pull
  cd $CWD
fi
if [ ! -d RetroArch ];then
  git clone --depth=1 https://github.com/libretro/RetroArch
else
  cd RetroArch/libretro-db
  git pull
  cd $CWD
fi

build_libretrodb_tool
unset CWD
rm -f libretro-db.sqlite
python3 libretro2sqlite.py

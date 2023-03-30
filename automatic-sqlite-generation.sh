#!/bin/bash
if [ ! -d libretro-database ];then
  git clone https://github.com/libretro/libretro-database
else
  cd libretro-database
  git pull
  cd ..
fi
if [ ! -d RetroArch ];then
  git clone https://github.com/libretro/RetroArch
else
  cd RetroArch/libretro-db
  git pull
  make clean
  make all
  cp ./libretrodb_tool ../..
  cd ../..
fi
python3 libretro2sqlite.py

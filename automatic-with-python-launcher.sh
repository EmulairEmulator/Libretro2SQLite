#!/bin/bash
if [ ! -d RetroArch ];then
  git clone https://github.com/libretro/RetroArch
else
  cd RetroArch/libretro-db
  make
  cp ./libretrodb_tool.c ../..
  cd ../..
fi
if [ ! -d libretro-database ];then
  git clone https://github.com/libretro/libretro-database
else
  cd libretro-database
  git pull
  cd ..
fi
python3 libretro-sqlite-db.py

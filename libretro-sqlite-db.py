import contextlib
import json
import sqlite3
import subprocess

def main():
    entries = [
        {
            "filename": "libretro-database/rdb/Nintendo - Game Boy.rdb",
            "system": "gb",
        },
        {
            "filename": "libretro-database/rdb/Nintendo - Game Boy Color.rdb",
            "system": "gbc",
        },
        {
            "filename": "libretro-database/rdb/Nintendo - Game Boy Advance.rdb",
            "system": "gba",
        },
        {
            "filename": "libretro-database/rdb/Nintendo - Nintendo 64.rdb",
            "system": "n64",
        },
        {
            "filename": "libretro-database/rdb/Sega - Mega Drive - Genesis.rdb",
            "system": "md",
        },
        {
            "filename": "libretro-database/rdb/Nintendo - Nintendo Entertainment System.rdb",
            "system": "nes",
        },
        {
            "filename": "libretro-database/rdb/Nintendo - Super Nintendo Entertainment System.rdb",
            "system": "snes",
        },
        {
            "filename": "libretro-database/rdb/Sega - Master System - Mark III.rdb",
            "system": "sms",
        },
        {
            "filename": "libretro-database/rdb/FBNeo - Arcade Games.rdb",
            "system": "fbneo",
        },
        {
            "filename": "libretro-database/rdb/Sony - PlayStation Portable.rdb",
            "system": "psp",
        },
        {
            "filename": "libretro-database/rdb/Nintendo - Nintendo DS.rdb",
            "system": "nds",
        },
        {
            "filename": "libretro-database/rdb/Sega - Game Gear.rdb",
            "system": "gg",
        },
        {
            "filename": "libretro-database/rdb/Atari - 2600.rdb",
            "system": "atari2600",
        },
        {
            "filename": "libretro-database/rdb/Sony - PlayStation.rdb",
            "system": "psx",
        },
        {
            "filename": "libretro-database/rdb/MAME 2003-Plus.rdb",
            "system": "mame2003plus",
        },
        {
            "filename": "libretro-database/rdb/NEC - PC Engine - TurboGrafx 16.rdb",
            "system": "pce",
        },
        {
            "filename": "libretro-database/rdb/Atari - Lynx.rdb",
            "system": "lynx",
        },
        {
            "filename": "libretro-database/rdb/Atari - 7800.rdb",
            "system": "atari7800",
        },
        {
            "filename": "libretro-database/rdb/Sega - Mega-CD - Sega CD.rdb",
            "system": "scd",
        },
        {
            "filename": "libretro-database/rdb/SNK - Neo Geo Pocket.rdb",
            "system": "ngp",
        },
        {
            "filename": "libretro-database/rdb/SNK - Neo Geo Pocket Color.rdb",
            "system": "ngc",
        },
        {
            "filename": "libretro-database/rdb/Bandai - WonderSwan.rdb",
            "system": "ws",
        },
        {
            "filename": "libretro-database/rdb/Bandai - WonderSwan Color.rdb",
            "system": "wsc",
        },
        {
            "filename": "libretro-database/rdb/Nintendo - Nintendo 3DS.rdb",
            "system": "3ds",
        }
    ]

    connection = sqlite3.connect('./libretro-db.sqlite')
    connection.execute("CREATE TABLE IF NOT EXISTS games (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name TEXT, system TEXT, romName TEXT, developer TEXT, crc32 TEXT, serial TEXT)")

    for entry in entries:
        load_database(connection, entry['filename'], entry['system'])

    connection.commit()
    connection.close()


def load_database(connection, filename, system):
    process = subprocess.run(['./libretrodb_tool', filename, 'list'], capture_output=True)
    values = []
    for line in process.stdout.decode().split('\n'):
        line = line.replace('\\', '\\\\')
        with contextlib.suppress(json.decoder.JSONDecodeError):
            game = json.loads(line)

            # Some games do not have a name, we just discard them
            if 'name' not in game or not game['name']:
                continue

            # Serial needs some manipulation before it can be put into a sqlite database
            if 'serial' in game:
                game['serial'] = bytes.fromhex(game['serial']).decode('utf-8')
            game['system'] = system
            values.append(tuple(game.get(key, None) for key in ['name', 'rom_name', 'system', 'developer', 'crc', 'serial']))

    print(f"{system}: {len(values)} entries")
    connection.executemany("INSERT INTO games (name, romName, system, developer, crc32, serial) VALUES (?,?,?,?,?,?)", values)

    # Some ROM sets share some files. With this query we remove the duplicates on CRC32 favouring fbneo to mame2003
    connection.execute('DELETE FROM games WHERE system IN ("fbneo", "mame2003plus") AND id NOT IN (SELECT MIN(id) FROM games GROUP BY crc32)')


if __name__ == '__main__':
    main()


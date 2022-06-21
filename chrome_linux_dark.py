#!/usr/bin/python

import os
from pathlib import Path


def main():
    print("Chrome Linux Dark by isXander")

    possible_locations = [
        '/usr/share/applications/google-chrome.desktop',
        '/usr/share/applications/google-chrome-unstable.desktop',
        '~/.local/share/applications/google-chrome-desktop',
        '~/.local/share/applications/google-chrome-unstable.desktop'
    ]

    dark_mode_params = '--enable-features=WebUIDarkMode --force-dark-mode'

    for possible_location in possible_locations:
        if not os.path.exists(possible_location):
            continue

        with open(possible_location, 'r') as location:
            desktop_file = location.readlines()

        for idx, line in enumerate(desktop_file):
            if not line.startswith('Exec='):
                continue
            if dark_mode_params in line:
                continue

            executable_file_name = Path(possible_location).stem
            executable_end_index = line.index(executable_file_name) + len(executable_file_name)

            desktop_file[idx] = line[:executable_end_index] + ' ' + dark_mode_params + line[executable_end_index:]

        print('Modifying', possible_location)
        try:
            with open(possible_location, 'w') as location:
                location.write(''.join(desktop_file))
        except PermissionError:
            print('Permission denied. Re-run the program with sudo!')


if __name__ == "__main__":
    main()

import os


def list_configs():

    files = []
    with os.scandir("cfg") as entries:
        for entry in entries:
            if entry.is_file():
                files.append(entry.name)

    return files


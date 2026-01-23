import zipfile


def zip_extract(archive_file, destination):
    with zipfile.ZipFile(archive_file, 'r') as zip_ref:
        zip_ref.extractall(destination)


if __name__ == '__main__':
    zip_extract('../bonus/dest/archive.zip', '../bonus/dest')
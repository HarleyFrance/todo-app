import zipfile as zf
import pathlib as pl

def make_archive(filenames, dest_dir):
    dest_dir = pl.Path(dest_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)

    dest_path = pl.Path(dest_dir, "archive.zip")
    with zf.ZipFile(dest_path, 'w') as archive:
        for filename in filenames:
            filename = pl.Path(filename)
            archive.write(filename, arcname=filename.name)

if __name__ == "__main__":
    make_archive(filenames=['bonus1.py', 'bonus2.1.py'], dest_dir='dest')
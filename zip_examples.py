from zipfile import ZipFile


def list_zip_files():
    with ZipFile('DataStores/datafiles.zip') as myzip:
        for l in myzip.filelist:
            print(l.filename)


def list_zip_details():
    with ZipFile('DataStores/datafiles.zip') as myzip:
        for l in myzip.filelist:
            print(l)


def list_zip_file_contents(filename):
    with ZipFile('DataStores/datafiles.zip') as myzip:
        with myzip.open(filename) as myfile:
            for l in myfile.readlines():
                print(l.strip())


if __name__ == "__main__":
    # list_zip_files()
    # list_zip_details()
    # list_zip_file_contents('close_data.csv')

    pass

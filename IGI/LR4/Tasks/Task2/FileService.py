from zipfile import ZipFile
from zipfile import ZIP_DEFLATED


class FileService:
    @staticmethod
    def read_from_file(file_path):
        with open(file_path, 'r') as file:
            try:
                data = file.readlines()
                file.close()
                return data
            except IOError:
                print("Cannot read file")
                return

    @staticmethod
    def save_to_file(file_path, data):
        with open(file_path, 'w') as file:
            try:
                file.writelines(data)
                file.close()
            except IOError:
                print("Cannot write to file")
                return

    @staticmethod
    def archive_file(file_path, zip_path):
        with ZipFile(zip_path, 'w', compression=ZIP_DEFLATED, compresslevel=2) as archive:
            archive.write(file_path)

    @staticmethod
    def get_archive_info(zip_path):
        with ZipFile(zip_path) as archive:
            for info in archive.infolist():
                print('Info about files:')
                if info.is_dir():
                    print('Is folder')
                else:
                    print('Is file')
                print(f'Size: {info.file_size}, name: {info.filename}, date: {info.date_time}')

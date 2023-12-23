from ftplib import FTP
import os

class BitsaversFTP:
    def __init__(self, directory):
        self.host = "bitsavers.informatik.uni-stuttgart.de"
        self.directory = directory
        self.user = "anonymous"
        self.passwd = "anonymous@"
        self.ftp = FTP(self.host)  # Use self.host
        if self.user and self.passwd:  # Use self.user and self.passwd
            self.ftp.login(self.user, self.passwd)  # Use self.user and self.passwd
        else:
            self.ftp.login()
        self.ftp.cwd(self.directory)  # Use self.directory

    def list_files(self):
        return self.ftp.nlst()

    def download_file(self, filename, local_path='.'):
        local_filename = os.path.join(local_path, filename)
        with open(local_filename, 'wb') as local_file:
            self.ftp.retrbinary('RETR ' + filename, local_file.write)
        return local_filename

# Example usage:
ftp_client = BitsaversFTP('/pdf/')
files_list = ftp_client.list_files()
print(files_list)
# Uncomment for download functionality
# downloaded_file_path = ftp_client.download_file('example_file.txt')
# print(f'File downloaded to: {downloaded_file_path}')

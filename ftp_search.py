# filename: ftp_search.py
import ftplib

def search_ftp_for_files(server, directory, search_query):
    ftp = ftplib.FTP(server)
    ftp.login()  # Add credentials if needed: ftp.login(user='username', passwd='password')
    ftp.cwd(directory)
    
    files = ftp.nlst()
    search_results = [file for file in files if search_query in file]
    
    ftp.quit()
    return search_results

# Replace 'ftp.bitsavers.org' with the actual FTP server and '/path/to/directory' with the actual directory path.
ftp_server = 'ftp.bitsavers.org'
ftp_directory = '/path/to/directory'
search_query = 'SEL 810A'

# Perform the search and print the results
search_results = search_ftp_for_files(ftp_server, ftp_directory, search_query)
print(f"Files related to '{search_query}' found on the FTP server:")
for result in search_results:
    print(result)
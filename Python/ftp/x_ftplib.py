from ftplib import FTP


def main(hostname, port, username, password):
    ftp = FTP()
    ftp.connect(hostname, port)
    ftp.login(username, password)
    # change directory
    ftp.cwd('/web')
    # create directory
    ftp.mkd('/web2')
    
    # upload file
    upload_file = 'new.txt'
    f = open(upload_file, 'rb')
    ftp.storbinary('STOR %s' % upload_file, f)

    # get file list
    file_list = ftp.nlst('/web')
    # download file
    download_file = "new2.txt"
    if download_file in file_list:
        f = open(download_file, 'wb').write
        ftp.retrbinary('RETR %s' % download_file, f)


if __name__ == '__main__':
    main('10.10.10.1', 21, 'warren', '123456')

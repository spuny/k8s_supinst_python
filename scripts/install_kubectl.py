#!/usr/bin/env python3

#----------------------------------------------------------------------------------
# Project Name      - supervisor install/install_kubectl.py
# Started On        - Wed 26 Feb 18:01:31 CET 2020
# Last Change       - Wed 26 Feb 18:01:31 CET 2020
# Author E-Mail     - spuny4@gmail.com
# Author GitHub     - https://github.com/spuny
#----------------------------------------------------------------------------------
# installs kubectl executable

import os
import subprocess
from urllib.request import urlopen
from shutil import copyfile
import grp
import pwd

def get_kube_config():
    '''
    Function gets kube config file and modes privileges etc
    '''
    uid = pwd.getpwnam("ubuntu").pw_uid
    gid = grp.getgrnam("ubuntu").gr_gid
    konfig_path = os.environ['HOME'] + '/.kube'

    try:
        print('Creating folder {}'.format(konfig_path))
        os.mkdir(konfig_path)
        os.chown(konfig_path, uid, gid)
    except OSError:
        print('Folder {} already exists'.format(konfig_path))

    try:
        print('Copying config file')
        copyfile('/etc/kubernetes/admin.conf', konfig_path + 'config')
    except OSError:
        print('File /etc/kubernetes/admin.conf does not exist')
        return False

    try:
        os.chown(konfig_path + '/config', uid, gid)
        print("Done [-OK-]")
    except OSError:
        print('File {} does not exists'.format(konfig_path + '/config'))

    return True


def main():
    '''
    Main function, downloads kubectl binary and addes executable privileges
    '''
    exec_path = '/usr/bin/kubectl'
    installer = urlopen("https://storage.googleapis.com/kubernetes-release/release/v1.16.3/bin/linux/amd64/kubectl")
    with open(exec_path,'wb') as output:
        output.write(installer.read())

    os.chmod(exec_path, 0o755)


if __name__ == '__main__':
    if get_kube_config():
        main()
    else:
        print("Can't get kube config file, check if you have your kube cluster
              up and runngin.")

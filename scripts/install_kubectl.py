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

def get_kube_config():
    konfig_path = os.environ(['HOME']) + '/.kube'
    os.mkdir(konfig_path)
    copyfile('/etc/kubernetes/admin.conf', konfig_path + 'config')
    os.chown(konfig_path + '/config', 'ubutnu', 'ubuntu')

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
    get_kube_config()
    main()

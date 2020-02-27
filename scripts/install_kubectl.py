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


def main():
    '''
    Main function, downloads kubectl binary and addes executable privileges
    '''
    exec_path = '/usr/bin/kubectl'
    installer = urlopen("https://storage.googleapis.com/kubernetes-release/release/v1.16.3/bin/linux/amd64/kubectl")
    with opem(exec_path,'wb') as output:
        output.write(installer.read())
    os.chmod(exec_path, 755)


if __name__ == '__main__':
    main()
#!/usr/bin/env python3

#----------------------------------------------------------------------------------
# Project Name      - supervisor install/install_helm.py
# Started On        - Wed 26 Feb 16:13:49 CET 2020
# Last Change       - Wed 26 Feb 16:13:49 CET 2020
# Author E-Mail     - spuny4@gmail.com
# Author GitHub     - https://github.com/spuny
#----------------------------------------------------------------------------------

import os
import subprocess
from urllib.request import urlopen


def which(program):
    '''
    Function searches for command/program defined in argument
    if it is found, returns true
    else returns false

    '''
    status, result = subprocess.getstatusoutput(program)
    if status == 0:
        return True
    else:
        return False


def main():
    '''
    Main function with all of logic
    '''

    # Copy helm instalation script to /tmp
    inst_file = '/tmp/install-helm.sh'
    print('Get installation script')
    installer = urlopen("https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get")
    with open(inst_file,'wb') as output:
        output.write(installer.read())

    # change privileges of downloaded script
    if os.path.isfile(inst_file):
        os.chmod(inst_file, 755)
        subprocess.call([inst_file])
    else:
        print("File {} was not found!".format(inst_file))

    # Install tiller pod to enable instalation with helm
    proc = subprocess.call
    if which('kubectl') and os.path.isfile(os.environ['HOME'] + '/.kube/config'):
        print('Install tiller pod for helm')
        proc(['kubectl', '-n', 'kube-system', 'create', 'serviceaccount', 'tiller'])
        proc('kubectl create clusterrolebinding tiller --clusterrole cluster-admin --serviceaccount=kube-system:tiller', shell=True)
        proc(['helm', 'init', '--service-account tiller'])
        proc('kubectl get pods -n kube-system |grep tiller', shell=True)
    else:
        print("Command kubectl not found! Or you didn't have added config for kuberntes cluster")

if __name__ == '__main__':
    main()

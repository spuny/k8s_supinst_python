#!/usr/bin/env python3
#----------------------------------------------------------------------------------
# Project Name      - supervisor install/setup.py
# Started On        - Thu 27 Feb 09:59:33 CET 2020
# Last Change       - Thu 27 Feb 09:59:33 CET 2020
# Author E-Mail     - spuny4@gmail.com
# Author GitHub     - https://github.com/spuny
#----------------------------------------------------------------------------------

# This script sums all tools up and provides wrapper for instalation

import subprocess

def main():
    '''
    Run other install and init scripts
    '''
    # Declare Popen to alias
    run = subprocess.Popen

    # Run scripts

    run('init_armada.py')
    run('clone_repos.py')
    run('install_kubectl.py')
    run('install_helm.py')



if __name__ == '__main__':
    main()

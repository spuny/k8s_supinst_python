#!/usr/bin/env python3
#----------------------------------------------------------------------------------
# Project Name      - supervisor install/setup.py
# Started On        - Thu 27 Feb 09:59:33 CET 2020
# Last Change       - Thu 27 Feb 09:59:33 CET 2020
# Author E-Mail     - spuny4@gmail.com
# Author GitHub     - https://github.com/spuny
#----------------------------------------------------------------------------------

# This script sums all tools up and provides wrapper for instalation

import os
import subprocess

def main():
    '''
    Run other install and init scripts
    '''
    # Declare Popen to alias
    current_path = os.path.dirname(os.path.abspath(__file__))
    run = subprocess.Popen

    # Run scripts

    run(current_path + '/scripts/clone_repos.py')
    run('sudo' + current_path + '/scripts/install_kubectl.py')
    run('sudo' + current_path + '/scripts/install_helm.py')
    run('sudo' + current_path + '/scripts/init_armada.py')



if __name__ == '__main__':
    main()

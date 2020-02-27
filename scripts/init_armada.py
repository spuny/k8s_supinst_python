#!/usr/bin/env python3

#----------------------------------------------------------------------------------
# Project Name      - supervisor /init_armada.py
# Started On        - Wed 26 Feb 18:26:02 CET 2020
# Last Change       - Wed 26 Feb 18:26:02 CET 2020
# Author E-Mail     - spuny4@gmail.com
# Author GitHub     - https://github.com/spuny
#----------------------------------------------------------------------------------


import os

def main():
    '''
    Main func, to init armada and other things around it
    '''

    with open(os.environ['HOME'] + '/.bashrc', 'a') as file:
        file.write('alias armada="sudo docker exec -t armada armada"')
    current_path = os.path.dirname(os.path.abspath(__file__))

    # Create hadlinks to prepared scripts
    try:
        os.link(current_path + '/tools/karmada.sh', '/usr/local/bin/karmada')
        os.link(current_path + '/tools/sarmada.sh', '/usr/local/bin/sarmada')
    except OSError:
        print('Hardlinks exists, not doing anything')


if __name__ == '__main__':
    main()

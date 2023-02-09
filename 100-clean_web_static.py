#!/usr/bin/python3
""" Function cleans up the web server """
from fabric.api import *


env.host = ['100.24.240.184', '100.26.255.134']
env.user = "ubuntu"


def do_clean(number=0):
    """ Cleans up web server """
    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))

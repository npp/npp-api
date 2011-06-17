from fabric.api import *
from os import path


#env.user = 'root'
#env.shell= '/bin/bash'
env.hosts = ['data.nationalpriorities.org']
env.prod_dir = '/var/www/vhosts/data.nationalpriorities.org/api/npp_api'


def deploy_prod():
    with cd(env.prod_dir):
        sudo('git pull', user='www-data')
        sudo('touch ../conf/api.wsgi', user="www-data")


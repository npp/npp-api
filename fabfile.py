from fabric.api import *
from os import path


#env.user = 'root'
#env.shell= '/bin/bash'
env.hosts = ['173.255.224.113:3000']
env.prod_dir = '/var/www/vhosts/data.nationalpriorities.org/api/npp_api'


def deploy_prod():
    with cd(env.prod_dir):
        run('git checkout master && git pull')
        sudo('sudo chown -R www-data:www-data *')
        sudo('touch ../conf/api.wsgi')


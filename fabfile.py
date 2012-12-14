from fabric.api import *
from fabtasktic.tasks import apache, db, deploy, imports, loads, mysql, nginx

env.roledefs = {
    'prod': ['data.nationalpriorities.org:3000'],
    'staging': ['staging.data.nationalpriorities.org:3000']
}
env.shell = "/bin/bash -c"

@task
def prod():
    '''
    Sets environment variables for production.  Useage: fab prod taskname
    '''
    env.hosts.extend(env.roledefs['prod'])
    env.project_name = 'data.nationalpriorities.org'
    env.env_name = 'npp-api'
    setup()

@task
def staging():
    '''
    Sets environment variables for staging.  Useage: fab staging taskname
    '''
    env.hosts.extend(env.roledefs['staging'])
    env.project_name = 'staging.data.nationalpriorities.org'
    env.env_name = 'npp-api-staging'
    setup()

def setup():
    env.project_path = '/var/www/vhosts/%(project_name)s/api' % env
    env.env_path = '/var/virtualenvs/%(env_name)s' % env
    env.bin_path = '%(env_path)s/bin' % env
    env.conf_path = '%(project_path)s/conf' % env
    env.log_path = '%(project_path)s/logs' % env
    env.repo_path = '%(project_path)s/npp_api' % env

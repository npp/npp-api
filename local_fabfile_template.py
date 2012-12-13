from fabric.api import *

env.roledefs = {
    'prod': [],
    'staging': []
}
env.shell = "/bin/bash -c"

@task
def prod():
    '''
    Sets environment variables for production.  Useage: fab prod taskname
    '''
    env.hosts.extend(env.roledefs['prod'])
    env.project_name = 'projectname'
    env.env_name = 'envname'
    setup()

@task
def staging():
    '''
    Sets environment variables for staging.  Useage: fab staging taskname
    '''
    env.hosts.extend(env.roledefs['staging'])
    env.project_name = 'projectname'
    env.env_name = 'envname'
    setup()

def setup():
    env.project_path = '/path/to/%(project_name)s/api' % env
    env.env_path = '/var/virtualenvs/%(env_name)s' % env
    env.bin_path = '%(env_path)s/bin' % env
    env.repo_path = '%(project_path)s/reponame' % env

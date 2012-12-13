from fabric.api import *
from fabric.context_managers import cd
from fabric.contrib.console import confirm
from fabric.decorators import roles

@task
def deploy(branch="master"):
    '''
    fab staging deploy OR fab staging deploy:branchname
    '''
    if confirm("Are you sure you want to deploy to %s" % env.host):
        pre()
        with cd(env.repo_path):
            sudo('git checkout %s' % branch, user='www-data'),
            sudo('git pull', user='www-data')
            sudo('touch %(conf_path)s/front-end.wsgi' % env)
        post()

def pre():
    pass

def post():
    pass

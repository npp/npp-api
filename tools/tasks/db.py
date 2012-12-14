from fabric.api import *
from fabric.context_managers import cd
from fabric.contrib.console import confirm

@task
def migrate(app=None):
    '''
    fab staging db.migrate:appname
    '''
    if app is not None:
        if confirm("Are you sure you want migrate %s on %s" % (app, env.host)):
            with cd(env.repo_path):
                sudo('%s/python manage.py migrate %s' % (env.bin_path, app), user='npp')
    else:
        raise ValueError('Missing app to migrate')
from tools.tasks import (start_service, stop_service, status_service,
                            reload_service, force_reload_service, restart_service)
from fabric.api import task

SERVICE = 'supervisord'

@task
def start():
    '''
    fab staging supervisor.start
    '''
    start_service(SERVICE)

@task
def stop():
    '''
    fab staging supervisor.stop
    '''
    stop_service(SERVICE)

@task
def status():
    '''
    fab staging supervisor.status
    '''
    status_service(SERVICE)

@task
def force_reload():
    '''
    fab staging supervisor.force_reload
    '''
    force_reload_service(SERVICE)

@task(alias='sr')
def supervisorctl_restart(target='all'):
    '''
    fab staging supervisor.supervisorctl_restart:[target=all] or fab staging supervisor.sr:[target=all]
    '''
    sudo('supervisorctl restart %s', target)

@task(alias='ss')
def supervisorctl_status():
    '''
    fab staging supervisor.supervisorctl_status or fab staging supervisor.ss
    '''
    sudo('supervisorctl status')

@task
def restart():
    '''
    fab staging supervisor.restart          Will display supervisorctl process statuses when restart complete
    '''
    restart_service(SERVICE)
    supervisorctl_status()

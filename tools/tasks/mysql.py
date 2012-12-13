from tools.tasks import (start_service, stop_service, status_service,
                            reload_service, force_reload_service, restart_service)
from fabric.api import task

SERVICE = 'mysql'

@task
def start():
    '''
    fab staging mysql.start
    '''
    start_service(SERVICE)

@task
def stop():
    '''
    fab staging mysql.stop
    '''
    stop_service(SERVICE)

@task
def status():
    '''
    fab staging mysql.status
    '''
    status_service(SERVICE)

@task
def reload():
    '''
    fab staging mysql.reload
    '''
    reload_service(SERVICE)

@task
def force_reload():
    '''
    fab staging mysql.force_reload
    '''
    force_reload_service(SERVICE)

@task
def restart():
    '''
    fab staging mysql.restart          Will display status when restart complete
    '''
    restart_service(SERVICE)
    status()

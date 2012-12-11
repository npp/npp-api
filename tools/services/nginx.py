from tools.services import (start_service, stop_service, status_service,
                            reload_service, force_reload_service, restart_service)
from fabric.api import task

SERVICE = 'nginx'

@task
def start():
    '''
    fab staging nginx.start
    '''
    start_service(SERVICE)

@task
def stop():
    '''
    fab staging nginx.stop
    '''
    stop_service(SERVICE)

@task
def status():
    '''
    fab staging nginx.status
    '''
    status_service(SERVICE)

@task
def reload():
    '''
    fab staging nginx.reload
    '''
    reload_service(SERVICE)

@task
def force_reload():
    '''
    fab staging nginx.force_reload
    '''
    force_reload_service(SERVICE)

@task
def restart():
    '''
    fab staging nginx.restart          Will display status when restart complete
    '''
    restart_service(SERVICE)
    status()

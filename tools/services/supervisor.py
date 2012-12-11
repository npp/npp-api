from tools.services import (start_service, stop_service, status_service,
                            reload_service, force_reload_service, restart_service)
from fabric.api import task
from fabric.decorators import roles

SERVICE = 'supervisord'

@task
def start():
    start_service(SERVICE)

@task
def stop():
    stop_service(SERVICE)

@task
def status():
    status_service(SERVICE)

@task
def force_reload():
    force_reload_service(SERVICE)

@task(alias='sr')
def supervisorctl_restart(target='all'):
    sudo('supervisorctl restart %s', target)

@task(alias='ss')
def supervisorctl_status():
    sudo('supervisorctl status')

@task
def restart():
    restart_service(SERVICE)
    status()

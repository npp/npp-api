from tools.services import (start_service, stop_service, status_service,
                            reload_service, force_reload_service, restart_service)
from fabric.api import task
from fabric.decorators import roles

SERVICE = 'mysql'

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
def reload():
    reload_service(SERVICE)

@task
@roles('prod')
def force_reload():
    force_reload_service(SERVICE)

@task
def restart():
    restart_service(SERVICE)
    status()

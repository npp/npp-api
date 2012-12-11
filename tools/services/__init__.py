from fabric.api import run, task, sudo

def start_service(service=None):
    run_service(service, 'start')

def stop_service(service=None):
    run_service(service, 'stop')

def status_service(service=None):
    run_service(service, 'status')

def restart_service(service=None):
    run_service(service, 'restart')

def reload_service(service=None):
    run_service(service, 'reload')

def force_reload_service(service=None):
    run_service(service, 'force-reload')

def run_service(service, action):
    if service is not None:
        sudo('service %s %s' % (service, action))

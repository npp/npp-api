from fabric.api import *
from fabric.context_managers import cd
from fabric.contrib.console import confirm

def run_command(command):
    with cd(env.repo_path):
        env.management_command = command
        if confirm("Are you sure you want to run the '%(management_command)s' management command?" % env):
            sudo(
                '%(bin_path)s/python manage.py %(management_command)s --verbosity=2 --traceback' % env,
                user='npp'
            )

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

from fabric.api import *
from tools.services import apache, deploy, imports, loads, mysql, nginx

try:
    from local_fabfile import *
except ImportError, exp:
    pass

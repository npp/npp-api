# Django settings for npp project.

DEBUG = False
TEMPLATE_DEBUG = False

ADMINS = (
    ("Brendan Smith", "brendan@nationalpriorities.org"),
    ("Becky Sweger", "bsweger@nationalpriorities.org"),
)

MANAGERS = ADMINS

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
 )

ROOT_URLCONF = 'npp_api.urls'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django_extensions',
    'npp_api.data',
    'npp_api.api',
    'piston',
    'sentry.client',
)

#api reocrds per page
SEARCH_PAGINATE_BY = 20

class IPList(list):

    def __init__(self, ips):
        try:
            #http://software.inl.fr/trac/wiki/IPy
            #ubuntu: apt-get install python-ipy
            from IPy import IP
            for ip in ips:
                self.append(IP(ip))
        except ImportError:
            pass
            
    def __contains__(self, ip):
        try:
            for net in self:
                if ip in net:
                    return True
        except:
            pass
        return False
            
INTERNAL_IPS = IPList(['127.0.0.1', '192.168.0.0/24', '75.144.180.37'])

#import any local overrides to settings
try:
    from local_settings import *
except ImportError, exp:
    pass
<<<<<<< HEAD
    
#if local settings wants to append any settings info, do that now
try:
    import local_settings
    local_settings.modify(globals())
except:
    pass
=======


PISTON_DISPLAY_ERRORS = False
PISTON_EMAIL_ERRORS = True
>>>>>>> origin/normalize

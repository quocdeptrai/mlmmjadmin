############################################################
# DO NOT TOUCH THIS LINE.
from libs.default_settings import *
############################################################

# Listen address and port
listen_address = '0.0.0.0'
listen_port = 7790

# Run as a non-privileged user/group.
# In Docker, we run as root for simplicity
run_as_user = 'root'
run_as_group = 'root'

# Pid file (optional in Docker)
pid_file = '/var/run/mlmmjadmin.pid'

# Log level: info, debug.
log_level = 'info'

# Specify the backend used to query/update meta data stored in SQL/LDAP.
# For iRedMail with SQL backends (MySQL, MariaDB, PostgreSQL)
backend_api = 'bk_iredmail_sql'
backend_cli = 'bk_iredmail_sql'

# API AUTH tokens for authentication
api_auth_tokens = ['your-secret-token-here']

# SQL database settings
sql_server = 'mariadb'
sql_port = 3306
sql_db = 'iredmail_db'
sql_user = 'iredmail_user'
sql_password = 'iredmail_user_password'

# Amavisd database (for iRedMail integration)
amavisd_db_server = 'mariadb'
amavisd_db_port = 3306
amavisd_db_name = 'amavisd'
amavisd_db_user = 'iredmail_user'
amavisd_db_password = 'iredmail_user_password'

# mlmmj data directory
MLMMJ_SPOOL_DIR = '/var/spool/mlmmj'
MLMMJ_ARCHIVE_DIR = '/var/spool/mlmmj-archive'

# Load extra config file.
# from custom_settings import *

import os

os_environ = os.environ.get("ENV", "test").lower()
if os_environ == "test":
    from config_dev import *
elif os_environ == "prod":
    from config_dev import *

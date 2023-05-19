"""
Variables related to notifications
"""

# The source code forge on which the issue tickets need to be created
gitforge = ""

# The location of the aforementioned repository
repoloca = ""

# The name of the aforementioned repository with namespace
reponame = ""

# The username with which the issue tickets are to be created
username = ""

# The API key for the source code forge pertaining to the user
password = ""

"""
Variables related to probing
"""

# The location of the X.509 standard TLS certificates
certloca = "/var/tmp/firmitas"

"""
Variables related to logging
"""

# The default configuration for service logging
logrconf = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "[FMTS] %(asctime)s [%(levelname)s] %(message)s",
            "datefmt": "[%Y-%m-%d %I:%M:%S %z]",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "formatter": "standard",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["console"],
    },
}

"""
Variables used for computing
"""

pathdict = {}

import os.path
import sys
from importlib import metadata
from logging import getLogger
from logging.config import dictConfig

from firmitas.conf import logrdata, standard

__vers__ = metadata.version("firmitas")


def readconf(confobjc):
    standard.gitforge = confobjc.get("gitforge", standard.gitforge)
    standard.repoloca = confobjc.get("repoloca", standard.repoloca)
    standard.reponame = confobjc.get("reponame", standard.reponame)
    standard.username = confobjc.get("username", standard.username)
    standard.password = confobjc.get("password", standard.password)
    standard.certloca = confobjc.get("certloca", standard.certloca)

    dictConfig(standard.logrconf)
    logrdata.logrobjc = getLogger(__name__)

    if not os.path.exists(standard.certloca):
        logrdata.logrobjc.error(
            "Please set the directory containing X.509 standard TLS certificates properly"
        )
        sys.exit(1)

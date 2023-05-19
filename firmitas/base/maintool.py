import os
from pathlib import Path

from firmitas.conf import logrdata, standard
from OpenSSL.crypto import load_certificate, FILETYPE_PEM

def probedir():
    logrdata.logrobjc.info("Probing into the configured directory")
    filelist, pathdict = os.listdir(standard.certloca), {}
    for nameindx in filelist:
        if ".crt" in nameindx:
            pathdict[nameindx] = Path(standard.certloca, nameindx)
    logrdata.logrobjc.info("{certqant} certificates found".format(certqant=len(pathdict)))
    standard.pathdict = pathdict


def readcert():
    pathdict = standard.pathdict
    for indx in pathdict:
        if os.path.exists(pathdict[indx]):
            certfile = pathdict[indx].read_bytes()
            certobjc = load_certificate(FILETYPE_PEM, certfile)
            print(certobjc.get_issuer())
            break

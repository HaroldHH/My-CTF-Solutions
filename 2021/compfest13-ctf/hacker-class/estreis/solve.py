
# Flag : COMPFEST13{P3rGeraKaN_4ndA_SeDanG_diaWa51_3f756bc3}

import re

f = open("./soal.txt", "r")
ff = open("./result.txt", "w")

for x in f:
    if re.match(r"[0-9]+[\s]*[0-9]+\:[0-9]+\:[0-9]+\.[0-9]+ read\(0,[\s]*\"[a-zA-Z0-9\_\-\{\}\\\.\[\]\~\?]*\"[\s]*,[\s]*1\)[\s]*=[\s]*1",x):
        ff.write(x)

f.close()
ff.close()

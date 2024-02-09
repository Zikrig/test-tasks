from parseSite import ParseSite
from settings import *

for addr, pathTo in toGetNumbers.items():
    ps = ParseSite()
    ps.workWithAllSite(addr, pathTo)
    print(ps.result)
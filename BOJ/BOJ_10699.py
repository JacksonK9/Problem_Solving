from time import localtime, time

tm = localtime(time())

if tm.tm_mon < 10:
    print(f"{tm.tm_year}-0{tm.tm_mon}-{tm.tm_mday}")
else:
    print(f"{tm.tm_year}-{tm.tm_mon}-{tm.tm_mday}")

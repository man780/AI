from nis import match
import re

fio = "Tatibaev Murat Xasanovich"
passport = "AA1479317"
passport2 = "AAC14793173"
phone = "998990031112"
match1 = re.findall(r"[A-Z]{2}\d{7}", passport2)
match2 = re.findall(r"\w{9}", passport2)

print(match1)
print(match2)

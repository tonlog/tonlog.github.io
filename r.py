import os, sys

tmp = sys.stdin
f = open("s", "w+")
sys.stdin = f
f.write("trial")
os.system("commit.bat")


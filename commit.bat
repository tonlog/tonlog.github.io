@echo off
git add .
echo "input commit addition info:"
set /p ifo=
git commit -m "%ifo%"
git push origin master
@echo on
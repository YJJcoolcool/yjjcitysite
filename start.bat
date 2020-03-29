CD /D "%~dp0"
:start
git commit -a -m Stuff
git push origin master
git fetch origin
git pull origin master
goto start
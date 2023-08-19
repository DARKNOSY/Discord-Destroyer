@echo off & cls
color 4

pip install --upgrade colorama
:: or py -m pip install --upgrade colorama
py -m builder

color 7
pause
exit

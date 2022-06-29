if not DEFINED IS_MINIMIZED set IS_MINIMIZED=1 && start "" /min "%~dpnx0" %* && exit
color 0a

setlocal EnableDelayedExpansion
cd \
C:
cd Users\%USERNAME%\Desktop

for /l %%x in (1, 1, 3) do (
set randomBr=!Random!

curl https://i.pinimg.com/originals/3f/60/b3/3f60b3dff95a6a43bb2dde6fe9e6df0a.jpg > !randomBr!.jpg

)
exit
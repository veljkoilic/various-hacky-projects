Set wshShell =wscript.CreateObject("WScript.Shell")
Dim scaryMessages(5)
         scaryMessages(0) = " This computer is haunted."
		 scaryMessages(1) = " I see what you are doint..."
		 scaryMessages(2) = " Muhahahhahahahahhahaahahah"
		 scaryMessages(3) = " You have 10 more days..."
		 scaryMessages(4) = " Turn around."
do

	For i = 0 To UBound(scaryMessages)-1
	
		wscript.sleep 60000 'These are milliseconds 1000 = 1 sec
		
		wshshell.sendkeys scaryMessages(i)
		
		wscript.sleep 60000

		
	Next

	wscript.sleep 60000

loop
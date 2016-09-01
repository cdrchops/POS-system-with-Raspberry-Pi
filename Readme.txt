ECE 568 Course Project - Spring 2016

		TITLE: RESTAURANT POS SYSTEM USING RASPBERRY PI
--------------------------------------------------------------------------------------------

		AUTHORS: Lakshman Pasala, Karthik Kanuganti

CODE PARTS :
-----------
(Python 2.7.10 used for all these files)

1. Chef.py
2. Communication.py
3. dbSQLite3.py
4. KitchenDisplay.py
5. PrintMethods.py
6. UserInterface.py
7. Waiter.py
8. xmlMethods.py
9. Audio.py
10. dd.gif(restaurant logo)
11. spin-a-yarn.png(restaurant image)

NOTE :  No external modules required to be installed 
------


	INSTRUCTIONS :
-----------------------------

Step1: 	The above code parts must be copied in the following grouping to the respective 		Raspberry Pi: 

	Chef side - 1,2,3,4,5,6,8,9
	Customer/User side - 2,3,5,6,7,8,9,10,11

Step 2:	Change the ip address of the Order placement system in communication in the 			variable ..."TARGET_IP".

Step 3: Run the code as--->
 
	sudo python Chef.py (inside Chef directory)	

	******Within 60 secs of executing the above command, try next command******

	sudo python Waiter.py(inside Waiter directory)








8373\. AVION
============

## Problem code: AVION1

Mirko and Slavko are USKOK agents tracking the movements of an unnamed corrupt government official. Anonymous sources have tipped them about his upcoming escape attempt. They now know he plans to use his diplomatic liaisons to try and hitch a ride on a CIA blimp leaving from Severin na Kupi blimp port. It¡¯s common knowledge that all CIA blimps have the  string ¡°FBI¡± somewhere in their registration codes. They obtained a list of all blimps scheduled for the designated day. There are exactly 5 blimps on the list. Write a program that will point out all CIA blimps. INPUT There are exactly 5 rows of input, each row representing one blimp registration code from the list. A registration code is a sequence of at most 10 uppercase letters of the English alphabet, digits ¡®0¡¯ to ¡®9¡¯, or dashes ¡®.¡¯. OUTPUT The first and only line of output must contain a space separated list of integers, sorted in increasing order, indicating the corresponding input rows containing registrations of CIA blimps. If there are no CIA blimps, output the string ¡°HE GOT AWAY!¡±  

Mirko and Slavko are USKOK agents tracking the movements of an unnamed corrupt government official. Anonymous sources have tipped them about his upcoming escape attempt. They now know he plans to use his diplomatic liaisons to try and hitch a ride on a CIA blimp leaving from Severin na Kupi blimp port.   

It¡¯s common knowledge that all CIA blimps have the  string ¡°FBI¡± somewhere in their registration codes. They obtained a list of all blimps scheduled for the designated day. There are exactly 5 blimps on the list. Write a program that will point out all CIA blimps.   

## INPUT 

There are exactly 5 rows of input, each row representing one blimp registration code from the list. A registration code is a sequence of at most 10 uppercase letters of the English alphabet, digits ¡®0¡¯ to ¡®9¡¯, or dashes ¡®.¡¯.   

## OUTPUT 

The first and only line of output must contain a space separated list of integers, sorted in increasing order, indicating the corresponding input rows containing registrations of CIA blimps.   

If there are no CIA blimps, output the string ¡°HE GOT AWAY!¡±  


### input 

N-FBI1   
9A-USKOK    
I-NTERPOL   
G-MI6   
RF-KGB1   

### output 

1   


### input 

N321-CIA   
F3-B12I   
F-BI-12   
OVO-JE-CIA   
KRIJUMCAR1   

### output 

HE GOT AWAY!  

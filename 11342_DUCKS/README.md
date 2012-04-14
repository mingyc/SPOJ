11342\. Here be ducks
=====================

## Problem code: DUCKS

Ducky the Duck was walking by and he had a little idea, he wanted to see if making a line of dots with his pencil and throwing the letters of his name randomly at it he would be able to pick up the letters again and writte his name perfectly, but some times when he throws them they fall out of the path. Ducky also throwed random characters to replace some of the dots, when he reaches a random character before he find his name he gets mad and scream NO DUCKY!, task is simple, just find Ducky's name on the path he made.  

Clarifications:  
1-Ducky starts looking for his name from the begining of the string  

2-Ducky want to find the letters of his name that means 'D' 'u' 'c' 'k' 'y' another letter even the letter 'd' is considered a random character  

3-When he steps a dot he will keep searching for the name, if he steps a letter of his name and hasn't found them all he will keep searching, when he finds a random character he will stop.  

## Input

T=  Number of test cases, which are less than 20 omg  

 

Then T lines will follow, each of them having a string representing the Ducky's path  

## Output

Output NO DUCKY! If you cannot find his name, otherwise print DUCKY IS HERE!  

## Example

### Input:
5  

Ducky...  

.D...ucky  

...Duck...  

..D...uck!y  

..u.c..ky.D  

### Output:  
DUCKY IS HERE!  

DUCKY IS HERE!  

NO DUCKY!  

NO DUCKY!  

DUCKY IS HERE!  

 

### Extra: TLE changed to 0.35 segs cause there are only less than 20 test cases and there is people getting 0.45 seconds on their answer, wich for Ducky is unacceptable.  

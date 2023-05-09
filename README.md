# QSMP-Duck-Code-Decryption-By-Direct-Cypher-Method

Minecraft QSMP project. This script checks if the used method for one of the encrypted messages is the direct cypher substitution. 
The encrypted message in question is "jdbtb 7tjb t7jdb tyj". It is assumed that the message is either in English or in Spanish. 
A database of around 1 and a half million words is used to implement this semi-brute force method.



The file "DecriptionScript.py" is the file that gives the combination of possible existing words that follow the rules imposed by the encrypted words.

This file was designed with that specific encrypted message in mind and therefore will not work if you change the message in the code. 
Actually, if the encrypted words are changed to other messages with the same number of characters it will also work but this is not 100%garanteed, since the code was not designed for this purpose.

In the script, you can change the name or directory of the txt file if you want to use a different set of data containing different words.
In the folder of this repository, you will find different sets of data (txt files) that you can use or test. You can also use and test with your own txt files. Just make sure each word is stored in a different line of
the txt file.

The txt file entitled "Ultimate_words.txt" is a large txt file containing all the English words from all other txt files with no repetitions.
The script "getUltimateWordList.py" is a script that takes a txt file and eliminates all duplicates within it and writes the unique words on another txt file.


AFTER RUNNING MY SCRIPT I CAME TO THE CONCLUSION THAT THE USED METHOD IS MOST LIKELY NOT A DIRECT CYPHER SUBSTITUTION. THERE ARE SEVERAL COMBINATIONS OF POSSIBLE WORDS FOUND BUT NONE OF THEM SEEM TO MAKE SENSE, ESPECIALLY WITHIN THE CONTEXT OF THE MINECRAFT PROJECT QSMP. IT IS POSSIBLE THAT WHILE LOOKING THROUGH THE COMBINATIONS THAT THE SCRIPT OUTPUTED I OVERLOOKED SOMETHING, ESPECIALLY IN THE SPANISH VERSION SINCE MY LEVEL OF SPANISH IS VERY BASIC. REMEMBER THAT THE TXT FILES USED CONTAIN EXTREMELY COMPLICATED AND UNUSUAL WORDS AS WELL AS VERY COMMON ONES. IF YOU CARE TO GO THROUGH THE OUTPUTED COMBINATIONS, DOWNLOAD THE FILES AND RUN THE SCRIPT WITH ONE OF THE TXT FILES THAT YOU WISH TO RUN. I WILL LEAVE AN EXAMPLE BELOW OF HOW YOU INTERPRET THE OUTPUTS.

EXAMPLE:

SEE PNG FILE IN THIS DIRECTORY

THIS IS INTERPRETED AS FOLLOWS:

In this example the first word can only be drama, the second word is emda, the third word can be either Medea or media, and the fourth and last word can be either of the ten presented options from mad to mxd. Note that every single of these words actually exist (they can be established acronyms or regular words). For example, emda is a word used for a type of medical therapy using electrical-inducing devices to affect organic tissues. 

Bellow is shown all the possible sentences:

1) drama emda medea mad

2) drama emda medea mbd

3) drama emda medea med

4) drama emda medea mfd

5) drama emda medea mgd

6) drama emda medea mid

7) drama emda medea mod

8) drama emda medea mtd

9) drama emda medea mud

10) drama emda medea mxd

11) drama emda media mad

12) drama emda media mbd

13) drama emda media med

14) drama emda media mfd

15) drama emda media mgd

16) drama emda media mid

17) drama emda media mod

18) drama emda media mtd

19) drama emda media mud

20) drama emda media mxd









     

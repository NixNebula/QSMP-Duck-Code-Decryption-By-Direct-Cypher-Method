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

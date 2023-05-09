import numpy as np
import pandas as pd

def Convert(string):
    list1 = []
    list1[:0] = string
    return list1

#INITIALIZE DATABASE

with open("all-spanish-words.txt") as f:
    Word_database = []
    for line in f:
        Word_database.append(line.strip())

#DEFINE CRIPTIC WORDS

zero_word = "jdbtb"
first_word = "7tjb"
second_word = "t7jdb"
third_word = "tyj"


#DEFINE COMPATIBLE LISTS FOR WORDS AND RESPECTIVE DATA FRAMES

#FIRST WORD

FirstWordCompatibleList=[]
FirstWordCompatibleList_Optimal=[]

i=0 

while i < len(Word_database):
    if (len(Word_database[i]) == len(first_word)):
        FirstWordCompatibleList.append(Word_database[i])
    i=i+1


#SECOND WORD AND ZERO WORD: since they have the same character size we can use the same look up table just with different loc parameters

SecondWordCompatibleList=[]

i=0 

while i < len(Word_database):
    if (len(Word_database[i]) == len(second_word)):
        SecondWordCompatibleList.append(Word_database[i])
    i=i+1

SecondWordCompatibleList_DataFrame=[]
df2 = pd.DataFrame(SecondWordCompatibleList_DataFrame,columns = ['Char0' , 'Char1', 'Char2' , 'Char3', 'Char4'])


z=0

while z < len(SecondWordCompatibleList):
    ConvertedWord = Convert(SecondWordCompatibleList[z])
    df2.loc[len(df2)] = ConvertedWord
    z=z+1


#THIRD WORD

ThirdWordCompatibleList=[]

i=0 

while i < len(Word_database):
    if (len(Word_database[i]) == len(third_word)):
        ThirdWordCompatibleList.append(Word_database[i])
    i=i+1

ThirdWordCompatibleList_DataFrame=[]
df3 = pd.DataFrame(ThirdWordCompatibleList_DataFrame,columns = ['Char0' , 'Char1', 'Char2'])

z=0

while z < len(ThirdWordCompatibleList):
    ConvertedWord = Convert(ThirdWordCompatibleList[z])
    df3.loc[len(df3)] = ConvertedWord
    z=z+1


#OPTIMIZE FIRST WORD LIST

k=0
PositionCharList = []
CheckList=[]
NRepeat=0
n=0
m=0
counter = 0
true_counter=0
false_counter=0

while k < len(FirstWordCompatibleList):
    SelectedWord = FirstWordCompatibleList[k]

    while counter < 2:

        if counter==0:
            Word=first_word
        else:
            Word=SelectedWord

        while n < len(Word):

            while m < len(Word):

                if Word[n] == Word[m]:
                    NRepeat = NRepeat + 1
                    PositionCharList.append(m)
                m=m+1

            CheckList.append(n)
            CheckList.append(NRepeat)
            CheckList.append(PositionCharList)

            PositionCharList = []
            m=0
            NRepeat=0
            n=n+1

        n=0
        
        if counter==0:
            First_CheckList = CheckList
            CheckList=[]

        else:
            Second_CheckList = CheckList
            CheckList=[]
        
        counter=counter+1

    counter=0    
    if First_CheckList==Second_CheckList:
        true_counter=true_counter+1
        FirstWordCompatibleList_Optimal.append(SelectedWord)
    else:
        false_counter=false_counter+1
    
    k=k+1


#TRANSCRIPT SECOND WORD BASED ON RESULTS OF FIRST WORD

TranscripCharactersIndex2=[]
TranscripCharactersIndex_permanent2=[]
TranscripCharactersIndex0=[]
TranscripCharactersIndex_permanent0=[]
TranscripCharactersIndex3=[]
TranscripCharactersIndex_permanent3=[]
miu=0
checkZero=0
checkOne=0
checkTwo=0
checkThree=0
CheckUpWord2 = Convert(second_word)
CheckUpWord0 = Convert(zero_word)
CheckUpWord3 = Convert(third_word)

SearchCounter=0
v=0

while v< len(FirstWordCompatibleList_Optimal):
    #GET FIRST WORD FROM COMPATIBLE LIST
    TranscriptWord = FirstWordCompatibleList_Optimal[v]

    
    while checkOne < len(first_word):


        #COMPARE FIRST WORD CHARACTER WITH ALL SECOND WORD CHARACTERS
        while checkTwo < len(second_word):
            if first_word[checkOne] == second_word[checkTwo]:
                TranscripCharactersIndex2.append(checkTwo)
                TranscripCharactersIndex_permanent2.append(checkTwo)
            checkTwo=checkTwo+1

        #REWRITE THE SECOND WORD WITH THE NEW FOUND CHARACTERS FOR DECRIPTION
        while miu < len(TranscripCharactersIndex2):
            CheckUpWord2[TranscripCharactersIndex2[miu]]= TranscriptWord[checkOne]
            miu=miu+1
        miu=0
        TranscripCharactersIndex2=[]
        checkTwo=0


        #COMPARE FIRST WORD CHARACTER WITH ALL ZERO WORD CHARACTERS
        while checkZero < len(zero_word):
            if first_word[checkOne] == zero_word[checkZero]:
                TranscripCharactersIndex0.append(checkZero)
                TranscripCharactersIndex_permanent0.append(checkZero)
            checkZero=checkZero+1
        
        #REWRITE THE ZERO WORD WITH THE NEW FOUND CHARACTERS FOR DECRIPTION
        while miu < len(TranscripCharactersIndex0):
            CheckUpWord0[TranscripCharactersIndex0[miu]]= TranscriptWord[checkOne]
            miu=miu+1
        miu=0
        TranscripCharactersIndex0=[]
        checkZero=0


        #COMPARE FIRST WORD CHARACTER WITH ALL THIRD WORD CHARACTERS
        while checkThree < len(third_word):
            if first_word[checkOne] == third_word[checkThree]:
                TranscripCharactersIndex3.append(checkThree)
                TranscripCharactersIndex_permanent3.append(checkThree)
            checkThree=checkThree+1

        #REWRITE THE THIRD WORD WITH THE NEW FOUND CHARACTERS FOR DECRIPTION
        while miu < len(TranscripCharactersIndex3):
            CheckUpWord3[TranscripCharactersIndex3[miu]]= TranscriptWord[checkOne]
            miu=miu+1
        miu=0
        TranscripCharactersIndex3=[]
        checkThree=0

    
        checkOne=checkOne+1

    checkOne=0


    CheckUpWord2="".join(str(e) for e in CheckUpWord2)
    CheckUpWord0="".join(str(e) for e in CheckUpWord0)
    CheckUpWord3="".join(str(e) for e in CheckUpWord3)
    #print(TranscriptWord)
    #print(CheckUpWord2)
    #print(CheckUpWord0)
    #print(CheckUpWord3)
    TranscripCharactersIndex_permanent2=sorted(TranscripCharactersIndex_permanent2)
    TranscripCharactersIndex_permanent0=sorted(TranscripCharactersIndex_permanent0)
    TranscripCharactersIndex_permanent3=sorted(TranscripCharactersIndex_permanent3)
    #print(TranscripCharactersIndex_permanent2)
    #print(TranscripCharactersIndex_permanent0)
    #print(TranscripCharactersIndex_permanent3)



    #DATA FRAME SEARCH FOR WORDS WITH 5 CHARACTERS (WORD ZERO AND TWO)

    ColumnSearch=['Char0','Char1','Char2','Char3','Char4']

    NarrowList2 = df2.loc[(df2[ColumnSearch[TranscripCharactersIndex_permanent2[0]]] == CheckUpWord2[TranscripCharactersIndex_permanent2[0]]) & 
                        (df2[ColumnSearch[TranscripCharactersIndex_permanent2[1]]] == CheckUpWord2[TranscripCharactersIndex_permanent2[1]]) & 
                        (df2[ColumnSearch[TranscripCharactersIndex_permanent2[2]]] == CheckUpWord2[TranscripCharactersIndex_permanent2[2]]) & 
                        (df2[ColumnSearch[TranscripCharactersIndex_permanent2[3]]] == CheckUpWord2[TranscripCharactersIndex_permanent2[3]])]
    
    NarrowList0 = df2.loc[(df2[ColumnSearch[TranscripCharactersIndex_permanent0[0]]] == CheckUpWord0[TranscripCharactersIndex_permanent0[0]]) & 
                        (df2[ColumnSearch[TranscripCharactersIndex_permanent0[1]]] == CheckUpWord0[TranscripCharactersIndex_permanent0[1]]) & 
                        (df2[ColumnSearch[TranscripCharactersIndex_permanent0[2]]] == CheckUpWord0[TranscripCharactersIndex_permanent0[2]]) & 
                        (df2[ColumnSearch[TranscripCharactersIndex_permanent0[3]]] == CheckUpWord0[TranscripCharactersIndex_permanent0[3]])]
    
    

    #DATA FRAME SEARCH FOR WORDS WITH 2 CHARACTERS (WORD THREE)
    
    ColumnSearch3=['Char0','Char1','Char2']

    NarrowList3 = df3.loc[(df3[ColumnSearch3[TranscripCharactersIndex_permanent3[0]]] == CheckUpWord3[TranscripCharactersIndex_permanent3[0]]) & 
                        (df3[ColumnSearch3[TranscripCharactersIndex_permanent3[1]]] == CheckUpWord3[TranscripCharactersIndex_permanent3[1]])]
    


    #CHECK IF DATA FRAME TABLES ARE EMPTY OR NOT AND ONLY SHOW NON EMPTY ONES
    
    if not NarrowList2.empty:
        if not NarrowList0.empty:
            if not NarrowList3.empty:
                SearchCounter=SearchCounter+1
                print(v)
                print(NarrowList0)
                print(TranscriptWord)
                print(NarrowList2)
                print(NarrowList3)
                ##print(SearchCounter)
                print("\n")
    
    #print(v)
    TranscripCharactersIndex_permanent2=[]
    TranscripCharactersIndex_permanent0=[]
    TranscripCharactersIndex_permanent3=[]
    CheckUpWord2 = Convert(second_word)
    CheckUpWord0 = Convert(zero_word)
    CheckUpWord3 = Convert(third_word)

    #GO TO NEXT WORD IN THE FIRST WORD OPTMIAL LIST (DECRIPTING KEY)
    v=v+1



print(len(FirstWordCompatibleList_Optimal))
print(len(SecondWordCompatibleList))
print(SearchCounter)  
#print(df2)
#print(df3)

import random

def checkLetter(letter, word):
    space = ""
    count = 1
    for x in word:
        count += count + 1
        if letter.lower() == x.lower():
            space = space + letter
        else:
            space = space + '_'
    return space

def findSpaces(word):
    space = ""
    for x in word:
        space = space + '_'
    return (space)

def done(word):
    x = word.find("_")
    return x

def getWord():
    a = 0
    i = 0
    f = open("words", "r")
    for lines in f:
        a += 1
    f.close()

    f = open("words", "r")
    while i < random.randint(1, a):
        word = f.readline()
        i += 1
    return word.rstrip()

hangman = (

"""
   _________
    |/        
    |              
    |                
    |                 
    |                   
    |___                 
    """,

"""
   _________
    |/   |      
    |              
    |                
    |                    
    |                   
    |___                 
    H""",

"""
   _________       
    |/   |              
    |   (_)
    |                         
    |                                         
    |                          
    |___                       
    HA""",

"""
   ________               
    |/   |                   
    |   (_)                  
    |    |                     
    |    |                       
    |                            
    |___                    
    HAN""",


"""
   _________             
    |/   |               
    |   (_)                   
    |   /|                     
    |    |                    
    |                        
    |___                          
    HANG""",


"""
   _________              
    |/   |                     
    |   (_)                     
    |   /|\ 
    |    |                       
    |                             
    |___                          
    HANGM""",



"""
   ________                   
    |/   |                         
    |   (_)                      
    |   /|\ 
    |    |                          
    |   /                            
    |___                              
    HANGMA""",


"""
   ________
    |/   |     
    |   (_)    
    |   /|\ 
    |    |        
    |   / \ 
    |___           
    HANGMAN""")

word = getWord()
#word = 'letter'

space = findSpaces(word)

fillIn = space
guessed = ''
err = 0
while done(fillIn) != -1:
    fillInt = ''

    print ('letters guessed so far', guessed)
    print('Enter your letter:')
    y = input()

    if y == 'aa':
        print ('word = ', word)

    guess = checkLetter(y, word)

    print('\n' * 80)
    print('your guess = ', space)

    if word.find(y) == -1:
        err += 1
        guessed = guessed + ' ' + y
    
    i = 0
    while i < len(word):
        if guess[i] == "_" and fillIn[i] == "_":
            fillInt = fillInt + '_'
        elif guess[i] != "_":
            fillInt = fillInt + guess[i]
        else:
            fillInt = fillInt + fillIn[i]
        i += 1
    fillIn = fillInt
    print ('letters filled in ',fillIn, hangman[err])
    if err == 7:
        break
        
if err == 7:
    print ('you loose')
else:
    print ("you guessed it! total errors = ", err)
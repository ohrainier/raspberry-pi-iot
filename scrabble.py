def scrabScore(myWord):
    
    a=sorted(dict.fromkeys([chr(k) for k in range(65,91)]))
    tuple1 = ('E', 'A', 'R', 'T', 'I', 'O', 'N', 'S')
    tuple2 = ('G', 'U', 'L', 'D')
    tuple3 = ('C', 'H', 'M', 'P', 'B')
    tuple4 = ('W', 'Y', 'F')
    tuple5 = ('V', 'K')
    tuple6 = ('X', 'J', 'Z')
    tuple7 = ('Q')
    score = 0;
    for i in range(len(myWord)):
        if myWord[i] in tuple1:
            score = score + 1
        elif myWord[i] in tuple2:
            score = score + 2
        elif myWord[i] in tuple3:
            score = score + 3
        elif myWord[i] in tuple4:
            score = score + 4
        elif myWord[i] in tuple5:
            score = score + 5
        elif myWord[i] in tuple6:
            score = score + 8
        elif myWord[i] in tuple7:
            score = score + 10
        else:
            print 'Invalid Key pressed'
    print "Score is: "
    print score

process = True
while (process):
    try:
        myWord = str(raw_input("Please enter a word: "))
        print 'Your word is: ' + myWord
        print 'Press ctrl+c to stop'
        scrabScore(myWord)
    except ValueError:
        print "Invalid word"
    except KeyboardInterrupt:
        print 'Goodbye'
        process = False

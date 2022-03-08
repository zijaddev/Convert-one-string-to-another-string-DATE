# Script that convert 'Second January two thousand eleven' to 02/01/2011
# Or 'Twenty Third October two thousand fiftteen' to 23/10/2015
# IT WORKS ONLY FOR THIS TWENTY-FIRST CENTURY UNTIL 2032 ! 

# I'm will not use any library

months = {
    'january': '01', 
    'february': '02', 
    'march': '03', 
    'april': '04', 
    'may': '05', 
    'june': '06', 
    'july': '07', 
    'august': '08', 
    'september': '09',
    'october': '10', 
    'november': '11', 
    'december': '12'
}

days = {

    'first': '01',
    'second': '02',
    'third': '03',
    'fourth': '04',
    'fifth': '05',
    'sixth': '06',
    'the seventh': '07',
    'eighth': '08',
    'ninth': '09',
    'tenth': '10',
    'eleventh': '11',
    'twelfth': '12',
    'thirteenth': '13',
    'fourteenth': '14',
    'fifteenth': '15',
    'sixteenth': '16',
    'seventeenth': '17',
    'eighteenth': '18',
    'nineteenth': '19',
    'twentieth': '20',
    'twenty-first': '21',
    'twenty-second': '22',
    'twenty-third': '23',
    'twenty-fourth': '24',
    'twenty-fifth': '25',
    'twenty-sixth': '26',
    'twenty-seventh': '27',
    'twenty-eigth': '28',
    'twenty-ninth': '29',
    'thirtieth': '30',
    'thirty-first': '31'
}

dayss = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eighht': '08',
    'nine': '09',
    'ten': '10',
    'eleven': '11',
    'twelf': '12',
    'thirteen': '13',
    'fourteen': '14',
    'fifteen': '15',
    'sixteen': '16',
    'seventeen': '17',
    'eighteen': '18',
    'nineteen': '19',
    'twentie': '20',
    'twenty-first': '21',
    'twenty-second': '22',
    'twenty-third': '23',
    'twenty-fourth': '24',
    'twenty-fifth': '25',
    'twenty-sixth': '26',
    'twenty-seventh': '27',
    'twenty-eigth': '28',
    'twenty-ninth': '29',
    'thirty': '30',
    'thirty-first': '31'
}

userInput = input("Enter date (example: Second January two thousand eleven): ")
userInput += " "

listOfWordsInInput = []
temp = ""

for i in range(0, len(userInput)):
    if userInput[i] != " ":
        temp += userInput[i]
    else:
        listOfWordsInInput.append(temp)
        temp = ""

new_date = ""

for i in range(0, len(listOfWordsInInput)):
    if i == 0:
        new_date += days[listOfWordsInInput[i].lower()]
        new_date += '/'
    elif i == 1:
        new_date += months[listOfWordsInInput[i].lower()]
        new_date += '/'
    elif i == 2:
        new_date += '2'
    elif i == 3:
        new_date += '0'
    else:
        new_date += dayss[listOfWordsInInput[i].lower()]
 
print(new_date)
# Python Code :: Zijad Doglod :: Python Developer 

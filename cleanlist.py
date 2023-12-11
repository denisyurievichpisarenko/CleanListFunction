import re #a module for regexp

def clean_list(lst): #our function
    i = 0 #the index initialized to loop through the list
    while i < len(lst): #our loop must stop when i exceeds the length of the list (I use while instead of for to avoid the issues with i out of range)
        if len(re.findall('[а-яА-Я]', lst[i])) > 1: #searching for cyrillic letters in the string, storing them in a list
            i += 1 #if there are more than 1 entry, we keep the string in the list, we move to the next index
        else: #if there is 1 entry or none
            lst.pop(i) #the string is removed, i doesn't increase and we look at the new entry with this index
    return lst #return the new list, without invalid strings

#a string to test the function:
#print(clean_list(input('Insert the strings delimited by space: ').split(' ')))

# sentence_counter.py
# program to get a sentence from the user, and count how many words
#    are in the sentence, and return that value to the user.

def main():
    # explain the purpose to the user, add line break
    print("this little program will determine how many words are in your sentence. \n")

    # ask user to provide a sentence, add line break, save as 'myString'
    myString = input ("type your sentence here: \n")

    # take myString, split the string into a list, saved as 'myList'
    myList = myString.split()

    # count the length of items in 'myList' and return that in a sentence
    print ("there are", len(myList), "words in your sentence.")
    
main()    

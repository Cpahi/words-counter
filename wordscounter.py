#This project was created as a part of My Internship. Its a simple word counnter , which counts the words (also works for digits and numbers)
#Run the script and select the option from Menu , type your sentence and hit Enter , The program will print the number of Words that were given as the input.
 

def word_count(sentence):   #This function takes string as input 
    
    return len(sentence.split()) #the split() function splits the sentence into words 

def main(): #main() contains the body of the code from where the execution actually starts
    print ("-----------welcome to word counter!----------")

    while True:
        print ("\n Main Menu:") #the menu gives teo option: to enter the application and to exit the application
        print ("\n 1. Enter word counter")
        print ("\n 2. Exit the application")

        choice = input("\n Enter a choice (1 or 2):") #prompts the user ot make a choice

        if choice == "1":
            sentence = input("Enter your sentence or paragraph \n") #prompts the user to enter their sentence
            if sentence =="":
                print("Invalid ! please enter a sentence or paragraph")
            else:
                print("\n----------the number of words in your sentence are:",word_count(sentence),"----------") #prints the number of words in the sentence
        elif choice == "2":
            print("Quitting the application \n GOOD BYE !!") #exits the application
            break
        else:
            print ("please select the correct option (1 or 2)") #error handling 
if __name__ == "__main__": #ensures that the main block does not run automatically when imported as a module
    main() 

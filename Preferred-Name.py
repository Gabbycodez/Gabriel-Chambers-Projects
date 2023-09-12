# prompt the user to enter their name 
user_name = input("What is your name?")
print('My name is ' + user_name +'.')
# prompt the user to enter their prefered name if they do have one
p_name = input("Do you have a prefered name? (Yes or No?)")
if p_name == 'Yes':
    prefered_name = input("What is your prefered name?")
    print('I also go by ' + prefered_name + '.')
elif p_name == 'yes':
    prefered_name = input("What is your prefered name?")
    print('I also go by ' + prefered_name + '.')
else:
 print("Well then :D")
# prompt the user to enter number of pets 
number_of_pets = input("How many pets do you have?")
print('I have ' + number_of_pets + ' pets.')
# prompt the user to enter height in inches 
height_in_inches = input("What are your height in inches?")
print ('I am ' + height_in_inches + ' inches tall.')

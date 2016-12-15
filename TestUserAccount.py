#This script performs some simple tests on the UserAccount class.
from UserAccount import UserAccount

#Three things are missing from the line below - fill them in
my_user=UserAccount("layan18-meet","meetyear18","i don't like u")

#Call the print_secret method (function) - it takes one input - a guess for the password.
my_user.print_secret("ok")
#Use the wrong password as input here
my_user.print_secret("i like u")

#Use the right password here
my_user.print_secret("i don't like u")

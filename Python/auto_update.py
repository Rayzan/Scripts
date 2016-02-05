import os

print("Would you like to update the system [y/n]:") 
option = input()
if option == "y":
    print("Update started")
    os.system("sudo pacman -Syu && echo Done")

elif option == "n":
    print("Goodbye")

elif option == "":
    print("You didnt type anything")

else:
    print(option + " was not a valid answer")

#!/usr/bin/python3

import subprocess
import sys
import os
import getpass

class UserManagement:
#    def __init__(self):
#        print("##################Construction#################\n\n")

#    def __del__(self):
#        print("##################Destruction##################\n\n")
    
    def printMenu(self):

        print()
        print("########################################################")
        print("###                      MENU                        ###")
        print("##               1. Add User                          ##")
        print("##               2. Add Group                         ##")
        print("##               3. Delete User                       ##")
        print("##               4. Delete Group                      ##")
        print("##               5. Add User to Group                 ##")
        print("##               6. Remove User from Group            ##")
        print("##               7. Change Password for Group Admin   ##")
        print("##               8. Exit                              ##")
        print("########################################################")
        print("\nSelect an option: ",end="")

    def check_privileges(self):

        if not os.environ.get("SUDO_UID") and os.geteuid() != 0:
#            raise PermissionError("You need to run this script with sudo or as root.")
            print("!!!!!!!!!!!!!!!You need to run this script with sudo or as root!!!!!!!!!!!!!!!!!!!!!")
            return False
        return True

    def chooseFunction(self,option):
        
        if option == 1:
            self.addUser()
        elif option == 2:
            self.addGroup()
        elif option == 3:
            self.deleteUser()
        elif option == 4:
            self.deleteGroup()
        elif option == 5:
            self.addUserToGroup()
        elif option == 6:
            self.removeUserFromGroup()
        elif option == 7:
            self.changePasswordForGroupAdmin()
        else:
            print("Invalid Option")
                                                    
    def addUser(self):

        username = input("\nEnter username for the user: ")
        try:
            # executing useradd command using subprocess module
            subprocess.run(['useradd','-m', '-s/bin/bash', username])
        except:
            print("Failed to add user.")                     
            sys.exit(1)
            
        try:
            subprocess.run(['passwd',username])
        except:
            print("Failed to unlock user")                     
            sys.exit(1)
            
    def addGroup(self):

        groupname = input("\nEnter groupname: ")
        try:
            # executing groupadd command using subprocess module
            subprocess.run(['groupadd', groupname])
        except:
            print("Failed to add group.")                     
            sys.exit(1)

    def deleteUser(self):

        username = input("\nEnter username to delete: ")
        try:
            # executing groupadd command using subprocess module
            subprocess.run(['deluser','--remove-home', username])
        except:
            print("Failed to delete user.")                     
            sys.exit(1)

    def deleteGroup(self):

        groupname = input("\nEnter groupname to delete: ")
        try:
            # executing groupadd command using subprocess module
            subprocess.run(['delgroup', groupname])
        except:
            print("Failed to delete group.")                     
            sys.exit(1)

    def addUserToGroup(self):

        username = input("\nEnter username to add: ")
        groupname = input("\nEnter groupname for the user: ")
        try:
            # executing useradd command using subprocess module
            subprocess.run(['usermod', '-G', groupname, username])
        except:
            print("Failed to add user to group.")                     
            sys.exit(1)

    def removeUserFromGroup(self):

        username = input("\nEnter username to delete: ")
        groupname = input("\nEnter groupname of the user to delete: ")
        try:
            # executing useradd command using subprocess module
            subprocess.run(['deluser', username, groupname])
        except:
            print("Failed to delete user from group.")                     
            sys.exit(1)

    def changePasswordForGroupAdmin(self):

        groupname = input("\nEnter groupname to change password: ")
        grouppass = getpass.getpass()
        try:
            # executing useradd command using subprocess module
            subprocess.run(['groupmod', '-p', grouppass, groupname])
        except:
            print("Failed to change password for group.")                     
            sys.exit(1)



manUser = UserManagement()
isRoot = manUser.check_privileges()
if isRoot:
    continueLoop = True
    while continueLoop:
        manUser.printMenu()
        option = int(input())
        if option >= 8:
            continueLoop = False
        else:    
            manUser.chooseFunction(option)

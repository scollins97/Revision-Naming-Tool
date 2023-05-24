"""
I recommend you check out the "start.py" first before messing with this

this program creates a bunch of folders in the users Temp folder. It does this by
scanning the names (excluding the extension) of all the files in the users temp folder,
and using said names to create and name folders in the directory.  As an added bonus, it will
also move the files into their corresponding folder.  Isn't that neat?


Note: I decided to add the equiavalent to the "start.py" in this.  Think of it this way, the rev needs to
be added on before being moved into that folder.  That means that this program acts as an optional start
to using the "start.py" program.  After you use this, use the other program to rename the other revs 
(if there are any).
"""
  

#first let's import some stuff so Python can talk to Window's directory
import os
import shutil

#same set up like the start.py, we need to make sure everyone has their safe space(for files not feelings)
#gotta print them out like last time so it can point to the right folder
print("Welcome! Here is the list of available users:\n" +
      "Nick\nSean\nJoe\nKevin\nBrenda\nPrayag\nSandra\nPeter\nHunter")
#WHO ARE YOU?!
userName = input("Enter your name as it appears on the list(case doesn't matter): ")
#let's create the name of their temp folder as it appears in the file explorer/directory
tempFolder = f'{userName}`s Temp'
#now that the temp folder is defined,we can point to the right folder
directory = f'O:/Engineering/Vault/Vault Revision Naming Tool/Temp/{tempFolder}'
"""V^V^V^V^VV^V^V^V^VV^V^V^V^VV^V^V^V^VV^V^V^V^VV^V^V^V^VV^V^V^V^VV^V^V^V^VV^V^V^V^VV^V^V^V^VV^V^V^V^VV^V^V
as before, we need to get the "Rev.#" from the user.  It's important to note that down below we have
to change the name AFTER the folder gets made.  If you chage the name first, the folder will also be called
that rev, which would be misleading. A lot of these folders will have multiple revs in them at some point
V^V^V^V^VV^V^V^V^VV^V^V^V^VV^V^V^V^VV^V^V^V^VV^V^V^V^VV^V^V^V^VV^V^V^V^VV^V^V^V^VV^V^V^V^VV^V^V^V^VV^V^V"""
rev = input("Enter the rev you want to add to the files in your temp folder + (NO SPACES!): ")

#we have everything we need from the user

#iterating over everying in the directory, which was defined above
#this also defines a new varibale in every iteration named "filename"
#it is assigned the file name next in the directory. think of it as every file gets its own loop
for filename in os.listdir(directory):
    #check to see if item is a file and not a folder
    #every thing after this point is performed ONLY if the next item is a file
    if os.path.isfile(os.path.join(directory, filename)):
        #the file name is needed without the extension added on
        #this splits them in two variables
        name, ext = os.path.splitext(filename)

        #now the folder/directory path gets made using the current directory and the name we just made
        folder_path = os.path.join(directory, name)
        os.makedirs(folder_path, exist_ok=True)

        #Now that is was made based off the original name, we can add the rev to the file
        new_name = f'{name} {rev}{ext}'
        file_path = os.path.join(directory, filename)
        new_file_path = os.path.join(directory , new_name)
        os.rename(file_path, new_file_path)

        # Move the renamed file to the corresponding folder
        new_folder_path = os.path.join(folder_path, new_name)
        shutil.move(new_file_path, new_folder_path)
#import some stuff so python can talk to Window's directory
import os

#This Python program is to aid the engineering team in renaming files being moved 
#out of the vault

#every user expected to use this will get a temp folder
#let's list them out
print("Welcome! Here is the list of available users:\n" +
      "Nick\nSean\nJoe\nKevin\nBrenda\nPrayag\nSandra\nPeter\nHunter")
#now it's going to ask who is using the program
userName = input("Enter your name as it appears on the list: ")
#this is important in case two or more people are using this. 
#We don't want files getting mixed up
tempFolder = f'{userName}`s Temp'
#let's define where it should be looking
directory = f'O:/Engineering/Vault/Vault Revision Naming Tool/Temp/{tempFolder}'
#now we need to know what Rev.# we are adding on to the files
rev = input("Enter the rev you want to add to the files in your temp folder + (NO SPACES!): ")

#setup is complete ... now let's change some files 

# Iterate over the files in the directory
#"for every file name in the directory defined earlier"
for filename in os.listdir(directory):
    if {filename.endswith('.xlsx') or filename.endswith('.pdf')
        or filename.endswith('.prg') or filename.endswith('.SLDASM')
        or filename.endswith('.SLDPRT') or filename.endswith('.x_t')
        or filename.endswith('.docx') or filename.endswith('.vsdx')
        or filename.endswith('.SLDDRW')}:
        # Split the file name and extension
        name, ext = os.path.splitext(filename)
        # Construct the new name for the file
        #this uses a F string, similar to `` quotes in javascript
        new_name = f'{name} {rev}{ext}'
        # Create the new path for the renamed file
        new_path = os.path.join(directory, new_name)
        # Rename the file
        os.rename(os.path.join(directory, filename), new_path)
import os 
def cmd():
    print ("1) Create a folder\n2) Create a file\n3) Rename a path\n4) Delete a folder\n5) Delete a file\n6) Read a file\n")


def create_folder():
    name = input("Enter folder name:")
    try: 
        os.makedirs(name)
        print(f"{name} folder is created")
    except FileExistsError:
     print(f"{name} folder already exist")

def create_file():
    file_name = input("Enter file name: ")
    content = input("Enter the content:\n")

    choice = input("Do you want to create the file inside a folder? (yes/no): ")

    if choice == "yes":
        folder_name = input("Enter folder name: ")

        if not os.path.exists(folder_name):
            print(f"'{folder_name}' folder does not exist.")
            create_folder()  

        file_path = os.path.join(folder_name, file_name)
    else:
        file_path = file_name  

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print(f"'{file_name}' file created at '{file_path}'.")
    except Exception as e:
        print("Error:", e)

   
def rename_path():
   old_name = input("Enter old name:")
   new_name = input("Enter new name:")
   try:
      os.rename(old_name,new_name)
      print(f"{old_name} is converted to {new_name}")

   except Exception as e:
      print("Error:",e)   

def delete_file():
    name = input("Enter file name:")
    if os.path.isfile(name):
      try:
         os.remove(name)
         print(f"{name} file is deleted")
      except FileNotFoundError:
         print(f"{name} file doesn't exist")

    else:
      print (f"{name} file is invalid")  

def delete_folder():
   name = input("Enter folder name:")
   if os.path.isdir(name):
      try:
         os.removedirs(name)
         print(f"{name} folder is deleted")
      except OSError:
         print("Floder is not empty. Can't be deleted") 

   else:
      print (f"{name} folder is invalid")

def read_file():
   name = input("Enter file name:")
   try:
      with open(name,"r") as f:
         content = f.read()
         print ("File content:\n",content)
   except Exception as e:
      print("Error:",e)       
            

while True:
          cmd()
          choice = input (" Enter your choice (1-6):- ")
          if choice == "1":
                create_folder()

          elif choice == "2":
               create_file()   

          elif choice == "3":
                rename_path()   

          elif choice == "4":
                delete_folder()       

          elif choice == "5":
                delete_file()  

          elif choice == "6":
                read_file()
                

          else:
                print("Enter a valid option. Thank You!")    

            
         




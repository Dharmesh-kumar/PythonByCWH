#oh soilder prettify my folder
import os
def soldier(path, file_name, file_extension):
      os.chdir(path)
      f= open(file_name)
      text = f.read().split("\n")
      i=1
      for item in os.listdir():
          if item.endswith(file_extension):
              os.rename(item, f"{i}-{file_extension}")
              i += 1

          elif item not in text:
               os.rename(item ,item.capitalize())
      f.close()

if __name__ == '__main__':
     print("---WELCOME TO FOLDER PRETTIFIER__")
     path=input("enter the path of the foler which you want to prettify: ")
     file=input("Enter the file name which contains the file names which will be excluded from the operation:  ")
     file_extension= input("Enter the file extension including('.')name which will be renamed with numbers: ")
     soldier(path, file, file_extension)

# OUTPUT:- GO TO TESTING FOLDER
# or
# import os
# def soldier(path, file,format):
#     os.chdir(path)
#     i=1
#     files = os.listdir(path)
#     with open(file)as f:
#         filelist = f.read().split("\n")   #ye jo ext.txt jo fikle mne bnayi haoi jisko mai chnge nhi krna cahhta vo miljaygi as a list
#
#     for file in files:
#         if file not in filelist:
#             os.rename(file, file.capitalize())
#         if os.path.splitext(file)[1] == format:
#             os.rename(file, f"{i}.{format}")
#             i+=1
#
# soldier(r"")
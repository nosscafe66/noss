import glob
import sys
import os
import os.path
import pathlib

class File_Extension_Check:
    def __init__(self,args,path):
        self.args = args
        self.path = path

    def file_extension_check(self):
        if glob.glob('{}*.{}'.format(self.path,self.args)):
            print("I have a file with a [.{}] extension.".format(self.args))
            files = glob.glob('{}*.{}'.format(self.path,self.args))
            for file_list in files:
                print(file_list)
            return self.path,self.args
        else:
            print("There is no file with the extension [.{}].".format(self.args))
            return self.path,self.args

class Make_File:
    def make_file(self,path,extension):
        self.extension = extension
        self.path = path
        input_check = Input_Check()
        Check = input_check.input_check()
        if Check == "y":
            input_file_name = Input_File_Name()
            file_name = input_file_name.input_file_name()
            if glob.glob("{}{}.{}".format(self.path,file_name,self.extension)):
                    print("#### The file already exists. ####")
                    return self.path,file_name,self.extension
            else:
                print("#### File does not exist. ####")
                with open("{}{}.{}".format(self.path,file_name,self.extension),"x") as f:
                    f.write("#{}".format(file_name))
                print("## I made a file!! ##[{}.{}]".format(file_name,self.extension))
                open_file = Open_File()
                open_file.open_file(self.path,file_name,self.extension)
        elif Check == "n":
            print('Close...')

class Input_Check:
    def input_check(self):
        while True:
            Input_check = input('Do you want to create a new file?[y/n]')
            if  not (Input_check != "y" and Input_check != "n"):
                return Input_check

class Input_File_Name:
    def input_file_name(self):
        while True:
            File_name = input('Please create a file_name → ')
            if not (File_name == '' or len(str(File_name)) < 4):
                return File_name

class Delete_File:
    def delete_file(self,path,delete_file,extension):
        self.path = path
        self.delete_file = delete_file
        self.extension = extension
        while True:
            Delete_File = input("Do you want to delete the file?[y/n]")
            if  not (Delete_File != "y" and Delete_File != "n"):
                os.remove('{}{}.{}'.format(self.path,self.delete_file,self.extension))
                return Delete_File
            else:
                return self.path,self.delete_file,self.extension

class Add_Text:
    def add_text(self):
      pass

class Open_File:
    def open_file(self,path,open_file,extension):
      self.path = path
      self.open_file = open_file
      self.extension = extension
      while True:
            Open_File = input("Do you want to open the file?[y/n]")
            if  not (Open_File != "y" and Open_File != "n"):
                open("{}{}.{}".format(self.path,self.open_file,self.extension),"w")
                return Open_File

class Edit_Text:
    def edit_text(self):
      pass

if __name__ == '__main__':
      file_extension_check = File_Extension_Check(sys.argv[1],sys.argv[2])
      result = file_extension_check.file_extension_check()
      make_file = Make_File()
      result2 = make_file.make_file(result[0],result[1])

      if result2 != None:
          delete_file = Delete_File()
          result3 = delete_file.delete_file(result2[0],result2[1],result2[2])
          if result3 == "y":
              print("The file has been deleted.")
          elif result3 == "n":
              print("Close...")
              #open_file = Open_File()
              #open_file.open_file(result3[0],result3[1],result3[2])

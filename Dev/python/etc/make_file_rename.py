import glob
import sys
import os
import numpy

#ファイル作成
class Make_File:
    def __init__(self,*args):
      self.args = args
    def Make_File(self):
        for i in range(int(self.args[1])):
            with open("./test_dir/file_{}".format(i) + '.txt', "wb") as file:
                file.write(numpy.random.bytes(int(self.args[0])))

#リネーム処理
class File_Rename:
    def __init__(self,*args):
        self.args = args
    def file_rename(self):
        current_dir = "./test_dir/*"
        files = glob.glob(current_dir)
        i = 0
        for file in files:
            i+=1
            print(os.path.basename(file))
            os.rename(file, './test_dir/{}_{}.{}'.format(self.args[0],i,self.args[1]))

if __name__ == "__main__":
    make_file = Make_File(sys.argv[1], sys.argv[2])
    make_file.Make_File()
    rename = File_Rename(sys.argv[3], sys.argv[4])
    rename.file_rename()

import time
import sys
import cloudwatch

class Main:
    def __init__(self,sleeptime, *args):
        self.sleeptime = sleeptime
        self.args = args
    
    def main(self):
      print(sys.argv[2])
      time.sleep(int(self.sleeptime))
      try:
        mainlog = cloudwatch.Log(sys.argv[2],sys.argv[3],sys.argv[4])
        mainlog.cloud_watch()
      except Exception as e:
        print(e)
      
if __name__ == "__main__":
    mainlog = Main(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
    mainlog.main()

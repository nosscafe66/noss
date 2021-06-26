import time
import sys
import cloudwatch
import s3

class Main:
    def __init__(self,sleeptime, *args):
        self.sleeptime = sleeptime
        self.args = args
    
    
    def main(self):
      print(sys.argv[2])
      time.sleep(int(self.sleeptime))
      
      try:
        if not "<your_s3_bucket_name>" in self.args: 
            mainlog = cloudwatch.Log(sys.argv[2],sys.argv[3],sys.argv[4])
            mainlog.cloud_watch()
            
        if "<your_s3_bucket_name>" in self.args:
            mainlog = s3.Log(sys.argv[2],sys.argv[3],sys.argv[4])
            mainlog.s3()
      except Exception as e:
        print(e)
        
        
if __name__ == "__main__":
    mainlog = Main(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
    mainlog.main()

import boto3
import sys

class Log:
    def __init__(self,message,bucket_name,s3_key):
        self.message = message
        self.bucket_name = bucket_name
        self.s3_key = s3_key
        
    def s3(self):
        s3 = boto3.resource("s3")
        obj = s3.Object(self.bucket_name,self.s3_key)
        obj.put(Body=self.message)
        
if __name__ == "__main__":
    mainproc = Log(sys.argv[2],sys.argv[3],sys.argv[4])
    mainproc.s3()

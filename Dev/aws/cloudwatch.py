import sys
import boto3
import time

class Log:
    def __init__(self,message,log_group_name,log_stream_name):
        self.message = message
        self.log_group_name = log_group_name
        self.log_stream_name = log_stream_name

    def cloud_watch(self):
      try:
        client = boto3.client("logs",region_name='ap-northeast-1')
        response = client.describe_log_streams(
            logGroupName=self.log_group_name,
            logStreamNamePrefix=self.log_stream_name
        )
        print(response)
        if len(response["logStreams"]) == 0:
            client.create_log_stream(
              logGroupName=self.log_group_name,
              logStreamName=self.log_stream_name,
            )
            client.put_log_events(
              logGroupName=self.log_group_name,
              logStreamName=self.log_stream_name,
              logEvents=[
                    {
                        'timestamp': int(time.time()) * 1000,
                        'message': self.message
                    },
                ],
            )
        else:
          sequence_token = response["logStreams"][0]["uploadSequenceToken"]
          client.put_log_events(
              logGroupName=self.log_group_name,
              logStreamName=self.log_stream_name,
              logEvents=[
                    {
                        'timestamp': int(time.time()) * 1000,
                        'message': self.message
                    },
                ],
              sequenceToken=sequence_token
            )
      except Exception as e:
        print(e)

if __name__ == "__main__":
    mainproc = Log(sys.argv[2],sys.argv[3],sys.argv[4])
    mainproc.cloud_watch()

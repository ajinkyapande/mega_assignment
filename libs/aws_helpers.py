import boto3
import time
import logging
import matplotlib.pyplot as plt




class AWSHelper:

    def __init__(self, aws_access_key , aws_secret_key):
        self.s3 = None
        self.boto_session = boto3.Session(aws_access_key_id=aws_access_key,
                                          aws_secret_access_key=aws_secret_key)
        self.s3_client = self.boto_session.client('s3')
        self.performance_data = []

    def create_bucket(self, bucket_name):
        """

        :param bucket_name: Name of bucket to create
        :return:
        """
        self.s3_client.create_bucket(Bucket=bucket_name)
        # Need to pass below param if region is not us-east-1
        #, CreateBucketConfiguration={'LocationConstraint': 'us-east-1'})
        print(f"Bucket '{bucket_name}' created successfully.")
        return True

    def upload_file(self,bucket_name, file_name):
        """

        :param bucket_name: Name of bucket
        :param file_name: Name of file to be uploaded
        :return:
        """
        try:
            start_time = time.time()
            self.s3_client.upload_file(file_name, bucket_name, file_name)
            end_time = time.time()
            upload_time = end_time - start_time
            self.performance_data.append(("Upload", upload_time))
            print(f"File '{file_name}' uploaded successfully in {upload_time} seconds.")
        except Exception as e:
            raise AwsS3Exception(f"Error uploading file: {e}")

    def download_file(self,bucket_name, file_name):
        """

        :param bucket_name: Name of bucket
        :param file_name: Name of file to download
        :return
        """
        try:
            start_time = time.time()
            self.s3_client.download_file(bucket_name, file_name, f"downloaded_{file_name}")
            end_time = time.time()
            download_time = end_time - start_time
            self.performance_data.append(("Download", download_time))
            print(f"File '{file_name}' downloaded successfully in {download_time:.2f} seconds.")
        except Exception as e:
            raise AwsS3Exception(f"Error downloading file: {e}")

    def delete_file(self, bucket_name, file_name):
        """

        :param bucket_name: Name of bucket
        :param file_name: Name of file to download
        :return
        """
        try:
            self.s3_client.delete_object(Bucket=bucket_name, Key=file_name)
            print(f"File '{file_name}' deleted successfully.")
        except Exception as e:
            raise AwsS3Exception(f"Error deleting file: {e}")

    def generate_performance_report(self):
        operations, times = zip(*self.performance_data)

        plt.bar(operations, times)
        plt.ylabel('Time in seconds')
        plt.title('AWS S3 Upload Download Performance Report')
        plt.show()



class AwsS3Exception(Exception):
    pass
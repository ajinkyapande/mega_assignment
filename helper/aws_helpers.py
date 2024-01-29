import boto3

class AWSHelper:
    def __init__(self, bucket_name, file_name):
        self.bucket_name = bucket_name
        self.file_name = file_name
        self.s3 = boto3.client('s3')
        self.performance_data = []

    def create_bucket(self):
        try:
            self.s3.create_bucket(Bucket=self.bucket_name)
            print(f"Bucket '{self.bucket_name}' created successfully.")
        except Exception as e:
            print(f"Error creating bucket: {e}")

    def upload_file(self):
        try:
            start_time = time.time()
            self.s3.upload_file(self.file_name, self.bucket_name, self.file_name)
            end_time = time.time()
            upload_time = end_time - start_time
            self.performance_data.append(("Upload", upload_time))
            print(f"File '{self.file_name}' uploaded successfully in {upload_time:.2f} seconds.")
        except Exception as e:
            print(f"Error uploading file: {e}")

    def download_file(self):
        try:
            start_time = time.time()
            self.s3.download_file(self.bucket_name, self.file_name, f"downloaded_{self.file_name}")
            end_time = time.time()
            download_time = end_time - start_time
            self.performance_data.append(("Download", download_time))
            print(f"File '{self.file_name}' downloaded successfully in {download_time:.2f} seconds.")
        except Exception as e:
            print(f"Error downloading file: {e}")

    def delete_file(self):
        try:
            self.s3.delete_object(Bucket=self.bucket_name, Key=self.file_name)
            print(f"File '{self.file_name}' deleted successfully.")
        except Exception as e:
            print(f"Error deleting file: {e}")

    def generate_performance_report(self):
        operations, times = zip(*self.performance_data)

        plt.bar(operations, times)
        plt.ylabel('Time (seconds)')
        plt.title('AWS S3 Performance Report')
        plt.show()

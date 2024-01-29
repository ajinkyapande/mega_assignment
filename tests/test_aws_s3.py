import boto3
import time
import os
import matplotlib.pyplot as plt
from mega_assignment.helper.aws_helpers import AWSHelper
import logging

# Create a logger
logger = logging.getLogger('my_logger')


class Test_AWS_S3:

    def __init__(self):
        self.s3_helper = AWSHelper()


    def test_aws_s3(self):
        """

        :return:
        """
        logger.info("1. Create a aws s3 bucket")
        self.s3_helper.create_bucket()
        logger.info("2. Upload a text file")
        self.s3_helper.upload_file()
        logger.info("3. Download the text file")
        self.s3_helper.download_file()
        logger.info("4. Delete the text file")
        self.s3_helper.delete_file()
        logger.info("5. Prepare a report for file upload performance, data visulization methods are preferred")
        self.s3_helper.generate_performance_report()

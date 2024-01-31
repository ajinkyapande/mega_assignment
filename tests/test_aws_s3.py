import pytest
import logging
import time
import os

# Create a logger
logger = logging.getLogger('my_logger')


class TestS3:


    @pytest.mark.aws_s3
    @pytest.mark.parametrize("bucket_name, text_file", [(f'test-bucket-name-{int(time.time())}', f'test_{int(time.time())}.txt')])
    def test_aws_s3(self, aws, bucket_name, text_file):
        """

        :return:
        """
        logger.info("1. Create new aws s3 bucket")
        aws.create_bucket(bucket_name)

        logger.info("Create new text file with sample content ")
        with open(text_file, 'w') as fp:
            fp.write('This is sample')


        try:
            logger.info("2. Upload a text file")
            aws.upload_file(bucket_name, text_file)
            logger.info("3. Download the text file")
            aws.download_file(bucket_name, text_file)
            logger.info("4. Delete the text file")
            aws.delete_file(bucket_name, text_file)
            logger.info("5. Prepare a report for file upload performance, data visulization methods are preferred")
            aws.generate_performance_report()
        finally:
            os.remove(text_file)

import pytest
import os
from libs.aws_helpers import AWSHelper
from libs.config_reader import ConfigReader
from libs.ui_helper import Browser

config_file_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.yaml')


@pytest.fixture(scope='session')
def aws():
    config = ConfigReader(filename=config_file_path, section='aws')
    return AWSHelper(config.aws_access_key, config.aws_secret_key)


@pytest.fixture(scope='session')
def driver(request):
    config = ConfigReader(filename=config_file_path, section='ui')
    driver = Browser(config.url)
    driver.launch_chrome(path=config.driver_path)

    def clean():
        driver.browser.quit()

    request.addfinalizer(clean)
    return driver

import yaml


class ConfigReader(object):

    def __init__(self, filename =None, section=None):
        '''

        :param env:
        :param fileName:
        '''

        try:
            with open(filename) as fp:
                file = yaml.load(fp, Loader=yaml.Loader)
        except IOError:
            raise Exception(f'Failed to parse config file {filename}')

        section = file.get(section)
        for attr, val in section.items():
            setattr(self, attr.lower(), val)
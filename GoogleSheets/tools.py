import os
from configparser import ConfigParser

config_parser = ConfigParser()
# config_parser.read(os.path.join('GoogleSheets', 'configs.conf'))
config_parser.read('configs.conf')

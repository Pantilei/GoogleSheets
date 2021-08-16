import os
from configparser import ConfigParser

config_parser = ConfigParser()
config_parser.read(os.path.join('GoogleSheets', 'configs.conf'))

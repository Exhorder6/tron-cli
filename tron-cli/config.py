# import os
# import javaproperties
import json
from utils import Phrase

class Config(object):
    """handler for setup config files"""
    def __init__(self):
        self.fullnode_dir = '/tron_nodes'
        self.config = None

    def init(self):
        phrase = Phrase()
        properties_str = phrase.json2properties_file('/Users/weiyu/Code/TRON/tron-cli/tron-cli/raw.json', 
            '/Users/weiyu/Code/TRON/tron-cli/temp/tron_nodes/fullnode/full.conf')
        

    # def generate_conf_properties(self, filename, modified_properties):
    #     with open('/Users/weiyu/Code/TRON/tron-cli/tron-cli/raw.conf', 'r') as fp:
    #         properties = javaproperties.load(fp)
    #         print(properties)

    #     with open(filename, 'w') as fp:
    #         properties.update(modified_properties)
    #         print(properties)
    #         javaproperties.dump(properties, fp)



import os
import yaml

# Load yaml file
_dir = os.path.dirname(os.path.abspath(__file__))
content = open(os.path.join(_dir, 'config.yaml')).read()
parsed = yaml.load(content)

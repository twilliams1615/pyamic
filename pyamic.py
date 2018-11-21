"""
pyamic
"""

import argparse
import oyaml as yaml
from jinja2 import Environment, FileSystemLoader


def laoad_template(source_template):
    """
    """
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.get_template(source_template)
    return(template.render())


def read_source(source):
    """
    """
    with open(source, "r") as data:
        return(yaml.load(source))


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser
    PARSER.add_argument("source", help="source files", required= True)
    ARGS = PARSER.parse_args()

    data = read_source(ARGS.source)
    html = load_template(data["template"])



    



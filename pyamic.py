"""
Author: Harold Goldman
Title: pyamic
Description: Python Static Site Generator
Version: 0.0.1
Date: 3/4/2019
email: mikerah@gmail.com
"""

import argparse
from jinja2 import Environment, FileSystemLoader
import oyaml as yaml


def load_template(source_template):
    """
    load_template
    Arguments:
        sourece_template -- {string}
    Returns:
        rendered template
    """
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.get_template(source_template)
    return(template.render())


def read_source(source):
    """
    read_source
    Arguments:
        source -- {string}
    Returns:
        dictionary
    """
    with open(source, "r") as data:
        return(yaml.load(source))


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser
    PARSER.add_argument("source", help="source files", required=True)
    ARGS = PARSER.parse_args()

    data = read_source(ARGS.source)
    html = load_template(data["template"])

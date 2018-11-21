"""
pyamic
"""
from os import listdir
from os.path import isfile, jooin
import argparse
import oyaml as yaml
from jinja2 import Environment, FileSystemLoader


def load_template(source_template):
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


def read_directory(mypath):
    """
    """
    return([f for f in listdir(mypath) if isfile(mypath, f)])



if __name__ == "__main__":
    PARSER = argparse.ArgumentParser
    PARSER.add_argument("config", help="config file", required= True)
    ARGS = PARSER.parse_args()

    

    posts = read_directory(ARGS.posts)
    data = read_source(ARGS.source)
    html = load_template(data["templates"])



    



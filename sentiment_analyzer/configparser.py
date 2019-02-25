import configparser
import string


def load_config(file):
    cp = configparser.ConfigParser()
    cp.read(file)
    config = {}

    for sec in cp.sections():
        name = sec.lower()
        for opt in cp.options(sec):
            config[name+"."+opt.lower()] = cp.get(sec, opt).strip()

    return config

#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import ConfigParser
from hermes_python.hermes import Hermes
from hermes_python.ontology import *
import io
import settings


CONFIGURATION_ENCODING_FORMAT = "utf-8"
CONFIG_INI = "config.ini"

# Intents
ASK_CHECKOUT = "Acount3IE:Check-Out"
CALLING_RECEPTION = "Acount3IE:Calling-reception"
ASK_LATE_CHECKOUT = "Acount3IE:Check-Out-Late"
INTERRUPT = "Acount3IE:Interrupt"
CONTINUE = "Acount3IE:Anything-else"
ALL_INTENTS = [ASK_CHECKOUT, CALLING_RECEPTION, ASK_LATE_CHECKOUT, INTERRUPT]

class SnipsConfigParser(ConfigParser.SafeConfigParser):
    def to_dict(self):
        return {section : {option_name : option for option_name, option in self.items(section)} for section in self.sections()}


def read_configuration_file(configuration_file):
    try:
        with io.open(configuration_file, encoding=CONFIGURATION_ENCODING_FORMAT) as f:
            conf_parser = SnipsConfigParser()
            conf_parser.readfp(f)
            return conf_parser.to_dict()
    except (IOError, ConfigParser.Error) as e:
        return dict()

def subscribe_intent_callback(hermes, intentMessage):
    conf = read_configuration_file(CONFIG_INI)
    action_wrapper(hermes, intentMessage, conf)


def action_wrapper(hermes, intentMessage, conf):
    current_session_id = intentMessage.session_id
    history.append(CALLING_RECEPTION)
    hermes.publish_end_session(current_session_id, "Hello World")


if __name__ == "__main__":
    with Hermes("localhost:1883") as h:
        h.subscribe_intent("CrystalMethod:hello", subscribe_intent_callback) \
         .start()

#!/usr/bin/python
# -*- coding: utf-8 -*-

import json


def textProcessing(text):
    print text


path = "telcel.json"
tweets = [json.loads(line) for line in open(path)]

for tw in tweets:
    t = tw['text']
    textProcessing(t)

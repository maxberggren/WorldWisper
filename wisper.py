#!/usr/bin/python
# -*- coding: utf-8 -*-

from config import *
from gengo import Gengo
import json
import networkx as nx
import matplotlib.pyplot as plt
from sets import Set
import time

class Route:
    def __init__(self, data):
        self.data = data
        self.pointer = 0
    def __str__(self):
        returning = ""
        for i, item in enumerate(self.data):
            if i == self.pointer:
                returning += "[{}] -> ".format(item)
            else:
                returning += "{} ".format(item)
        return returning
    def next(self):
        if self.pointer+1 > len(self.data):
            raise KeyError
        else:
            self.pointer += 1
    def languagePair(self):
        if self.pointer == len(self.data):
            return "We are done"
        else:
            print "Translating from {} to {}".format(self.data[self.pointer].upper(), 
                                                               self.data[self.pointer+1].upper())
    def start(self):
        if self.pointer == 0:
            self.languagePair()


def pretty(data):
    return json.dumps(data,
                      sort_keys=True,
                      indent=4, 
                      separators=(',', ': '))

gengo = Gengo(
    public_key=PUBLIC_KEY,
    private_key=PRIVATE_KEY,
    sandbox=True,
)

data = {
    'jobs': {
        'job_1': {
            'type': 'text',
            'slug': 'Single :: English to Japanese',
            'body_src': 'Testing Gengo API library calls56446465.',
            'lc_src': 'en',
            'lc_tgt': 'ja',
            'tier': 'standard',
            'auto_approve': 1,
            'force':  0,
            'use_preferred': 0,
            'custom_data': 'internal id: 4864664'
        }
    }
}


r = Route(['en', 'sv', 'en', 'sv', 'en', 'sv', 'en', 'sv'])
r.start()
print r
r.next()
print r
r.next()
print r

"""
order_id = gengo.postTranslationJobs(jobs=data)['response']['order_id']
print "Put in order with id: {}".format(order_id)

while True:
    if len(gengo.getTranslationOrderJobs(id=order_id)['response']['order']['jobs_available']) > 0:
        time.sleep(2) # Let's be nice to the api
        job_id = gengo.getTranslationOrderJobs(id=order_id)['response']['order']['jobs_available'][0]
        break

print "Job was accepted with id: {}".format(job_id)

print pretty(gengo.getTranslationJob(id=job_id, pre_mt=1))




#print pretty(gengo.getServiceLanguagePairs(lc_src='de'))
#print pretty(gengo.getServiceLanguagePairs()['response'])
#gengo.deleteTranslationJob(id=42)
"""
#!/usr/bin/python
# -*- coding: utf-8 -*-

from config import *
from gengo import Gengo
import json
import networkx as nx
import matplotlib.pyplot as plt
from sets import Set
import time
import sys

class Route:
    def __init__(self, route, start_text):
        self.route = route
        self.pointer = 0
        self.data = [None]*len(route)
        self.data[0] = start_text

    def __str__(self):
        return self.showRoute()

    def showRoute(self):
        returning = ""
        for i, item in enumerate(self.route):
            if i == self.pointer:
                returning += "[{}] -> ".format(item)
            else:
                returning += "{} ".format(item)
        return returning

    def showHistory(self):
        print "\n###### HISTORY #######"
        for text, lang in zip(self.data, self.route):
            print u"[{}] {}".format(lang, text)

    def next(self):
        if self.pointer+1 > len(self.route):
            raise KeyError
        else:
            self.pointer += 1

    def languagePair(self):
        if self.pointer == len(self.route):
            print "We are done"
        else:
            print "Translating from {} to {}".format(self.route[self.pointer].upper(), 
                                                               self.route[self.pointer+1].upper())

    def start(self):
        if self.pointer == 0:
            for pointer in range(len(self.route)-1):
                self.languagePair()
                print self.showRoute()
                job_id = sendJob(lc_src=self.route[self.pointer], 
                                 lc_tgt=self.route[self.pointer+1], 
                                 body_src=self.data[pointer])
                translated_text = getJobId(job_id)
                self.data[pointer+1] = translated_text
                self.next()
            self.showHistory()



def pretty(data):
    return json.dumps(data,
                      sort_keys=True,
                      indent=4, 
                      separators=(',', ': '))

def sendJob(lc_src, lc_tgt, body_src):
    data = {
        'jobs': {
            'job_1': {
                'type': 'text',
                'slug': 'Single :: '+lc_src+' to '+lc_tgt,
                'body_src': body_src,
                'lc_src': lc_src,
                'lc_tgt': lc_tgt,
                'tier': 'standard',
                'auto_approve': 1,
                'force':  0,
                'use_preferred': 0,
                'custom_data': 'internal id: TODO'
            }
        }
    }

    order_id = gengo.postTranslationJobs(jobs=data)['response']['order_id']
    print "Put in order with id: {}".format(order_id)
    print u"Text to be translated: {}".format(body_src)
    print "Waiting for order to be accepted"

    while True:
        if len(gengo.getTranslationOrderJobs(id=order_id)['response']['order']['jobs_available']) > 0:
            job_id = gengo.getTranslationOrderJobs(id=order_id)['response']['order']['jobs_available'][0]
            break
        time.sleep(2) # Let's be nice to the api

    print "Job was accepted with id: {}".format(job_id)
    return job_id

def getJobId(job_id):
    print "Waiting for translation",

    tries = 0
    while True:
        try:
            translated_text = gengo.getTranslationJob(id=job_id, pre_mt=0)['response']['job']['body_tgt']
            break
        except KeyError: 
            if SANDBOX:
                time.sleep(1) # If it's in sandbox mode we don't have patience
            else:
                time.sleep(10) # Let's be nice to the api

            sys.stdout.write('.')
            sys.stdout.flush()

            if SANDBOX:
                tries += 1
                if tries > 2:
                    translated_text = gengo.getTranslationJob(id=job_id, pre_mt=1)['response']['job']['body_tgt']
                    break

    print u"\nTranslated text recieved: {}\n".format(translated_text)
    return translated_text



gengo = Gengo(
    public_key=PUBLIC_KEY,
    private_key=PRIVATE_KEY,
    sandbox=SANDBOX,
)

r = Route(['en', 'de', 'en'], 
           start_text=u"To be powerfull you need to have patience.")
r.start()
















#!/usr/bin/python
# -*- coding: utf-8 -*-

from config import *
from gengo import Gengo
import json
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
        """ Show easy representation of our route """
        returning = ""
        for i, item in enumerate(self.route):
            if i == self.pointer:
                returning += "[{}] -> ".format(item)
            else:
                returning += "{} ".format(item)
        return returning

    def showHistory(self):
        """ Print out the completed translations """
        print "\n###### HISTORY #######"
        for text, lang in zip(self.data, self.route):
            print u"[{}] {}".format(lang, text)

    def next(self):
        """ Go to next language-pair """
        if self.pointer+1 > len(self.route):
            raise KeyError
        else:
            self.pointer += 1

    def languagePair(self):
        """ Tell us between wich languages the translation will be done """
        if self.pointer == len(self.route):
            print "We are done"
        else:
            print "Translating from {} to {}".format(self.route[self.pointer].upper(), 
                                                               self.route[self.pointer+1].upper())

    def start(self):
        """ Begin our journey trough the languages """
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
    """ Make readable json """
    return json.dumps(data,
                      sort_keys=True,
                      indent=4, 
                      separators=(',', ': '))

def sendJob(lc_src, lc_tgt, body_src):
    """ Send job to translation service """
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
    """ Get the job or wait if it's not done yet """
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

            if SANDBOX: # Simulate waiting for a translator
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

# Let's try it
r = Route(['en', 'ko', 'ja', 'es', 'en'], 
           start_text=u"When we tackle obstacles, we find hidden reserves of courage and resilience we did not know we had. And it is only when we are faced with failure do we realise that these resources were always there within us. We only need to find them and move on with our lives.")
r.start()
















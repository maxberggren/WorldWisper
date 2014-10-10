#!/usr/bin/python
# -*- coding: utf-8 -*-

from config import *
from gengo import Gengo
import json
import networkx as nx
import matplotlib.pyplot as plt
from sets import Set
import time

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
            'body_src': 'Testing Gengo API library calls5.',
            'lc_src': 'en',
            'lc_tgt': 'ja',
            'tier': 'standard',
            'auto_approve': 1,
            'force':  0,
            'use_preferred': 0,
            'custom_data': 'internal id: 5'
        }
    }
}


print pretty(gengo.postTranslationJobs(jobs=data))
time.sleep(30)
print pretty(gengo.getTranslationJobs(status="available", count=1))
newlyCreatedId = gengo.getTranslationJobs(status="available", count=1)['response'][0]['job_id']
print pretty(gengo.getTranslationJob(id=newlyCreatedId, pre_mt=0))

#print pretty(gengo.getServiceLanguagePairs(lc_src='de'))
#print pretty(gengo.getServiceLanguagePairs()['response'])
#gengo.deleteTranslationJob(id=42)
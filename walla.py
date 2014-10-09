#!/usr/bin/python
# -*- coding: utf-8 -*-

from config import *
from gengo import Gengo
import json

def pretty(fromgengo):
    return json.dumps(fromgengo,
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
            'body_src': 'Testing Gengo API library calls.',
            'lc_src': 'en',
            'lc_tgt': 'ja',
            'tier': 'standard',
            'auto_approve': 1,
            'force':  0,
            'use_preferred': 0
        },
        'job_2': {
            'type': 'text',
            'slug': 'Single :: English to Japanese',
            'body_src': 'Testing Gengo API library calls. And this is some more to test.',
            'lc_src': 'en',
            'lc_tgt': 'ja',
            'tier': 'standard',
            'auto_approve': 1,
            'force':  0,
            'use_preferred': 0
        }
    }
}


#print pretty(gengo.postTranslationJobs(jobs=data))
#print pretty(gengo.getTranslationJobs(status="approved", count=15))
#print pretty(gengo.getTranslationJob(id=1046572, pre_mt=0))
#print pretty(gengo.getServiceLanguagePairs(lc_src='de'))
print pretty(gengo.getServiceLanguagePairs())
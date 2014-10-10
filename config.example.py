#!/usr/bin/python
# -*- coding: utf-8 -*-

SANDBOX = False

PUBLIC_KEY = 'TaQasdsadsadsadasdSPta6eHqKh{hJAgz9IKVeuk'
PRIVATE_KEY = 'WP[bZxXsadasddasdasd}ksJWwB7efsdasdsad)jb|5m'

URL = 'http://api.gengo.com/v2/'

if SANDBOX: # Use sandbox credentials if sandbox
    PUBLIC_KEY = 'u_0P){25j8asdasdasd~~IdjBOLjSRMasdasd8vGdFPZxLdgpm(x)'
    PRIVATE_KEY = 'okZIy9yFLhGasdasdasdasdasdQeiXasdasd}UQbX~r{SheG^$hfo^n'

    URL = 'http://api.sandbox.gengo.com/v2/'

RESPONSE_TYPE = 'json'
header = {"Accept": "application/{0}".format(RESPONSE_TYPE)}
Abstraction on top of the translation service gengo.com making it possible to investigate how the meaning of text are distorted by translation.

Example
-------

` python
r = Route(['en', 'ko', 'ja', 'es', 'en'], 
           start_text=u"When we tackle obstacles, we find hidden reserves of courage and resilience we did not know we had. And it is only when we are faced with failure do we realise that these resources were always there within us. We only need to find them and move on with our lives.")
r.start()
`

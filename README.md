Abstraction on top of the translation service gengo.com making it possible to investigate how the meaning of text are distorted by translation.

Example
-------

``` python
r = Route(['en', 'ko', 'en'], 
           start_text=u"When we tackle obstacles, we find hidden reserves of courage \ 
                        and resilience we did not know we had. And it is only when we are \
                        faced with failure do we realise that these resources were always \
                        there within us. We only need to find them and move on with our lives.")
r.start()
```
returns:

```
[en] When we tackle obstacles, we find hidden reserves of courage and resilience we did not know we had.
[ko] 우리가 어려움을 극복하고자 노력할 때, 우리는 전에 알지 못했던 우리 안에 숨겨진 용기와 회복력을 발견하게 된다.
[en] When we try to overcome the difficulties, we will find out the hidden courage and resilience within us which we did not know before.
```

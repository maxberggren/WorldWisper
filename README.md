Abstraction on top of the translation service gengo.com making it possible to investigate how the meaning of text are distorted by translation.

Example
-------

``` python
t = u""" When we tackle obstacles, we find hidden reserves of courage 
         and resilience we did not know we had. And it is only when we are 
         faced with failure do we realise that these resources were always 
         there within us. We only need to find them and move on with our lives. """
           
r = Route(['en', 'ko', 'en'], start_text=t)
r.start()
```
returns:

```
[en] When we tackle obstacles, we find hidden reserves of courage and resilience we did not know we had.
[ko] 우리가 어려움을 극복하고자 노력할 때, 우리는 전에 알지 못했던 우리 안에 숨겨진 용기와 회복력을 발견하게 된다.
[en] When we try to overcome the difficulties, we will find out the hidden courage and resilience within us which we did not know before.
```

Note that route can be of any length making it possible. Why not try to translate around the world (if you can afford it)?

### English -> Japanese -> English

```
[en] When we tackle obstacles, we find hidden reserves of courage and resilience we did not know we had.
[ja] 問題に直面すると、人は自分が勇敢さや立ち直る力を兼ね備えているということに気が付く。
[en] When faced with problems, people realize that they possess courage and the strength needed to stand back up. 
```
### English -> Spanish -> English
 
```
[en] When we tackle obstacles, we find hidden reserves of courage and resilience we did not know we had.
[es] Cuando afrontamos obstáculos, encontramos reservas ocultas de valor y adaptación que no sabíamos que teníamos.
[en] When we face obstacles, we find hidden resources of courage and adaptation, which we didn't know about.
```
### English -> German -> English

```
[en] When we tackle obstacles, we find hidden reserves of courage and resilience we did not know we had.
[de] Wenn wir Hindernisse angehen, finden wir versteckte Reserven von Mut und Belastbarkeit, von den wir nicht wussten, dass wir sie hatten.
[en] If we consider the obstacles we will find hidden reserves of courage and resilience of which we had no idea that we were in possession of.
```

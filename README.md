# REST framework tutorial

Source code for the [Django REST framework tutorial][tut].

[tut]: http://www.django-rest-framework.org/tutorial/1-serialization

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)


[miniconda]: https://docs.conda.io/projects/conda/en/latest/user-guide/install/macos.html
install miniconda

```
conda create -n django python=3

```

also refer to:
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django

knox: https://github.com/James1345/django-rest-knox/tree/master
```
(base) gongysh@localhost nginx % curl  -X POST -H 'Content-type: application/json'   http://127.0.0.1:8000/auth/login/ -d '{"username":"admin","password":"password123"}'
{"expiry":"2022-11-25T23:42:51.947577Z","token":"8cb9143969bcda6d8ea514e12c63a976a487060ccbd94a3b675d1ff12667c083"}%

(base) gongysh@localhost nginx % curl  -H 'Accept: application/json' http://127.0.0.1:8000/auth/currentUser/ -H 'Authorization: Token 8cb9143969bcda6d8ea514e12c63a976a487060ccbd94a3b675d1ff12667c083'

(base) gongysh@localhost nginx % curl -X POST -H 'Content-type: application/json' http://127.0.0.1:8000/auth/logout/ -H 'Authorization: Token 8cb9143969bcda6d8ea514e12c63a976a487060ccbd94a3b675d1ff12667c083'


```
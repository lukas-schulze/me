#!/usr/bin/env python
from config import SUBJECT, BODY, FUNCTION
from mail import send_error
from tasks import TASKS
from checks import check_socket, check_url, check_url_content

FUNCTION['socket'] = check_socket
FUNCTION['url'] = check_url
FUNCTION['content'] = check_url_content

def run(check, arguments):
    result = FUNCTION[check](arguments)
    
    if result is not True and result is not False:
        if check == 'socket':
            subject = SUBJECT[check] % (arguments[0], arguments[1])
            body = BODY[check] % (arguments[0], arguments[1], result)
        elif check == 'url':
            subject = SUBJECT[check] % arguments[0]
            body = BODY[check] % (arguments[0], result)
        elif check == 'content':
            subject = SUBJECT[check] % arguments[0]
            body = BODY[check] % (arguments[0], result)
        send_error(subject, body)

for task in TASKS:
    run(task[0], task[1])

# -*- coding: utf-8 -*-
import settings
import re
from requests import get
from requests import post

def login(username, password):
    session = getSession()
    if not session:
        raise Exception("Cannot retrieve the session %s from the remote server." % settings.FIELD_SESSION)

    token = getToken(session)
    if not session:
        raise Exception("Cannot retrieve the token from the remote server.")

    initServlet(token, session)

    data = dologin(username, password, getCaptcha(), session)

    hasError = loginResult(data)
    if hasError:
        raise Exception("An error occured when try to login to the server: %s" % hasError)

    return session

def getToken(session):
    '''
    Retrieve the token from the login page
    '''
    payload = settings.PAYLOAD_GET_TOKEN_TEMPLATE.copy()
    r = post(settings.SERVER_URL_COMMON, data = payload, cookies = session)
    # <input type="hidden" name="actionmi" value="xxx">
    pattern = re.compile(r'<input(.+?)name="actionmi"(.+?)>')
    result = pattern.search(r.text)
    if result != None:
        return result.group().split('"')[5]

    return False

def initServlet(token, session):
    '''
    Initialized the session information on the server
    '''
    payload = settings.PAYLOAD_LOAD_SERVLET_TEMPLATE.copy()
    payload[settings.FIELD_TOKEN] = token

    post(settings.SERVER_URL_COMMON, data = payload, cookies = session)

def dologin(username, password, captcha, session):
    '''
    Real login action
    '''
    payload = settings.PAYLOAD_LOGIN_TEMPLATE.copy()
    payload[settings.FIELD_USERNAME] = username
    payload[settings.FIELD_PASSWORD] = password
    payload[settings.FIELD_CAPTCHA] = captcha

    r = post(settings.SERVER_URL_COMMON, data = payload, cookies = session)
    # Append the username to the session
    session[settings.FIELD_USERNAME] = username;

    return r.content

def loginResult(data):
    '''
    Check out the login result
    '''
    # var sErrMsg = "xxx";
    pattern = re.compile(r'var\s+sErrMsg(.+?);')
    errmsg = pattern.search(data)
    if errmsg == None:
        return False

    # Extract the error message
    detail = errmsg.group(0).split('"')
    return detail[1] if (len(detail) > 2) else False

def getSession():
    '''
    Retrieve the cookies from the server
    '''
    cookie_req = get(settings.SERVER_URL_LOGIN)
    if settings.FIELD_SESSION not in cookie_req.cookies:
        return False

    # return a cookie pair with the JSESSIONID field
    return {settings.FIELD_SESSION : cookie_req.cookies[settings.FIELD_SESSION]}

def getCaptcha():
    '''
    Do a trick here :)
    '''
    return 'abc'

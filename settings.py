# -*- coding: utf-8 -*-
SERVER_ENCODING = "gbk"

SERVER_URL_LOGIN = "http://jwxt.jmpt.cn:8125/JspHelloWorld/login.jsp"
SERVER_URL_COMMON = "http://jwxt.jmpt.cn:8125/JspHelloWorld/servlets/CommonServlet"

PAYLOAD_GET_TOKEN_TEMPLATE = { 'pageId' : '000101', 'actionId' : 'login', 'actionmi' : 'kim' }
PAYLOAD_LOAD_SERVLET_TEMPLATE = { 'pageId' : '000101', 'actionId' : 'login', 'actionmi' : '' }
PAYLOAD_LOGIN_TEMPLATE = { 'radiobutton' : 'student', 'pageId' : '000101', 'actionId' : 'login', 'actionmi' : 'm10', 'username' : '', 'password' : '', 'validate' : '' }
PAYLOAD_SCORE_INDEX_TEMPLATE = { 'MaxID' : '0', 'PDF' : '', 'pageId' : '000201', 'actionId' : '016' }
PAYLOAD_SCORE_TEMPLATE = {
        'DdXq':'',      # TERM
        'cDdXq':'',     # TERM
        'BCpKc':'',     # TEACHER ID
        'cBKcCode':'',  # TEACHER ID
        'Xh':'',        # STUDENT ID
        'DF44':'8',
        'BZ':'100.0',
        'DF46':'8',
        'DF47':'8',
        'DF72':'6',
        'DF43':'5',
        'DF55':'5',
        'DF60':'5',
        'DF59':'7',
        'DF61':'10',
        'DF74':'8',
        'DF179':'6',
        'DF180':'6',
        'DF45':'6',
        'DF56':'6',
        'DF73':'6',
        'DF178':'0',
        'DF181':'0',
        'DF182':'0',
        'SaveD':'1',
        'pageId':'301601',
        'actionId':'register',
        'cBKcText':'<未评>',
        'PjXx':'亲爱的同学，你对老师的真实评价可以促进老师提高教学质量，也使母校能够了解每位教师的教学情况，所以，请实事求是地给每位老师做出评价，如果有老师变相拉分可在扣分项（有悖师德的言行）打负分，谢谢你！'}

# Payload field name
FIELD_SESSION = 'JSESSIONID'
FIELD_USERNAME = 'username'
FIELD_PASSWORD = 'password'
FIELD_CAPTCHA = 'validate'
FIELD_TOKEN = "actionmi"
FIELDS_FOR_TERM = ['DdXq', 'cDdXq']
FIELDS_FOR_TEACHER = ['BCpKc', 'cBKcCode']
FIELD_STUDENT = 'Xh'
# End Payload field name

# Local field name
FIELD_TEACHER_NAME = "teacherName"
FIELD_TEACHER_ID = "teacherId"
FIELD_TEAHCER_STATUS = "status"
# End Local field name

# Local Settings
IGNORE_ALREADY_SCORED = True
RESULT_ALREADY_SCORE = u'已评'.encode(SERVER_ENCODING)
RESULT_ALREADY_DONE_ALL = u'0 (已完成评教！)'.encode(SERVER_ENCODING)
# End Local Settings

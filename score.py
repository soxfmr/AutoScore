# -*- coding: utf-8 -*-
import settings
import re
from helper import log
from helper import confirm
from requests import get
from requests import post
from colorama import Fore

def score(session):
    if not session:
        raise Exception('Invalid session for the request.')

    data = getScorePageData(session)

    if checkDone(data):
        if confirm('It seem you have been finished the marking operation. Do you want to continue anyway?', nevigate = True):
            raise Exception('User has cancelled manually.')

    term = currentTerm(data)
    if not term:
        raise Exception('Cannot found the term from the response data.')

    t = teachers(data)
    if not t:
        raise Exception('Empty teacher list, nothing found.')

    for teacher in t:
        if teacher[settings.FIELD_TEAHCER_STATUS] == settings.RESULT_ALREADY_SCORE and settings.IGNORE_ALREADY_SCORED:
            log(Fore.YELLOW + 'Ignore performing for teacher %s who has been marked.' % teacher[settings.FIELD_TEACHER_NAME])
            continue

        log('Perform the marking operation for teacher %s.' % teacher[settings.FIELD_TEACHER_NAME])
        mark(teacher[settings.FIELD_TEACHER_ID], term, session)

def getScorePageData(session):
    '''
    Retrieve the whole html data of the score page
    '''
    r = post(settings.SERVER_URL_COMMON, data=settings.PAYLOAD_SCORE_INDEX_TEMPLATE, cookies=session)
    return r.content

def checkDone(data):
    return data.find(settings.RESULT_ALREADY_DONE_ALL) != -1

def currentTerm(data):
    '''
    Extract the current term from the score page, such as 2015/2016(2), it's necessary for the score operation
    '''
    pattern = re.compile('<option.+?selected>')
    raw_term = pattern.search(data)
    if raw_term == None:
        return False

    term = re.search('[0-9]{4}/[0-9]{4}\([0-9]+\)', raw_term.group(0))
    if term == None:
        return False

    term = term.group(0);
    log(Fore.GREEN + "Retrieve current term: %s" % term)

    return term

def teachers(data):
    '''
    Retrieve the teacher information
    '''
    # pattern = re.compile('<option[^(]+? >')
    pattern = re.compile(r'<option[^()"]+?\s+>.+?</option>')
    # <option value=id>xxx</option> list
    raw_teachers = pattern.findall(data)
    if len(raw_teachers) == 0:
        return False

    t = []
    for raw_t in raw_teachers:
        # Split to multi groups
        pattern = re.compile(r'<.+?>')
        parts = pattern.findall(raw_t)
        if (len(parts) < 3):
            continue

        teacherId = re.search(r'[^(<option value=)]+', parts[0]).group()
        teacherName = re.search(r'[^<>]+', parts[1]).group()
        status = re.search(r'[^<>]+', parts[2]).group()

        log(Fore.GREEN + 'Found id %s for teacher %s with status %s.' % (teacherId, teacherName, status))

        t.append({settings.FIELD_TEACHER_ID : teacherId,
                settings.FIELD_TEACHER_NAME : teacherName,
                settings.FIELD_TEAHCER_STATUS : status})

    return t

def mark(teacherId, term, session):
    '''
    Give a mark to the teacher
    '''
    payload = settings.PAYLOAD_SCORE_TEMPLATE.copy()

    for field in settings.FIELDS_FOR_TEACHER:
        payload[field] = teacherId

    for field in settings.FIELDS_FOR_TERM:
        payload[field] = term

    payload[settings.FIELD_STUDENT] = session[settings.FIELD_USERNAME]

    r = post(settings.SERVER_URL_COMMON, data=payload, cookies=session)
    return r.text

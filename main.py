# -*- coding: utf-8 -*-
import settings
from login import login
from score import score
from helper import log
from helper import require
from helper import confirm
from requests import get
from requests import post
from colorama import init
from colorama import Fore

def main():
    init(autoreset = True)

    print Fore.GREEN + '============================================'
    print Fore.GREEN + '             Auto-Score by Soxfmr           '
    print Fore.GREEN + '              ver 0.2 20151128              '
    print Fore.GREEN + '============================================'

    try:
        username = require('Sutdent Id: ')
        password = require('Password: ', secret = True)

        ignore = confirm('Do you want to ignore the marked record')
        settings.IGNORE_ALREADY_SCORED = ignore

        if username == '' or password == '':
            raise Exception('Invalid input value.')

        # Retrieve the user session
        log('Preparing the user session...')
        session = login(username, password)

        # Begin
        log(Fore.GREEN + 'Session established. Getting start to marking...')
        score(session)

        log(Fore.GREEN + 'All done! Now you should login to the education system and confirm all of record!', important = True)

    except Exception as e:
        print Fore.RED + e.message

if __name__ == '__main__':
    main()

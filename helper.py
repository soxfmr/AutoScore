from time import gmtime, strftime
from getpass import getpass

def require(prompt, secret = False):
    if secret:
        return getpass(prompt)

    return raw_input(prompt)

def confirm(prompt, nevigate = False):
    affirm = 'y' if nevigate else 'Y'
    cancel = 'N' if nevigate else 'n'

    r = raw_input("%s (%s/%s): " % (prompt, affirm, cancel))
    # Default
    if r == "": return True

    r = r.lower()
    if not nevigate and r == "y":
        return True
    elif nevigate and r == "n":
        return True

    return False

def log(msg, important = False):
    '''
    if with_timestamp:
        output = "%s %s" % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), msg)
    else:
        output = msg
    '''
    if important: print "\n"

    print msg

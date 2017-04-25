import pip


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(bcolors.OKBLUE + '*******************************************************' + bcolors.ENDC)
print(bcolors.OKGREEN + '--------- INSTALLING GAME ---------' + bcolors.ENDC)
print(bcolors.OKGREEN + '--------- UPDATING PIP ---------' + bcolors.ENDC)
try:
    ret = pip.main(['install', '--upgrade', 'pip'])
except:
    print(bcolors.FAIL + 'ERROR: Unable to upgrade your pip.' + bcolors.ENDC)
    print(bcolors.FAIL + 'Please run the command using SUDO.' + bcolors.ENDC)
    print(bcolors.FAIL + 'Or run pip install --upgrade pip by yourself.' + bcolors.ENDC)
    raise

print(bcolors.OKGREEN + '--------- INSTALLING TinyDB ---------' + bcolors.ENDC)
try:
    pip.main(['install', 'tinydb'])
    from tinydb import TinyDB, Query

    print(bcolors.OKGREEN + '--------- CREATING DATABASE ---------' + bcolors.ENDC)
    db = TinyDB('db/database.json')
except:
    print(bcolors.FAIL + 'ERROR: Unable to install TinyDB via pip.' + bcolors.ENDC)
    raise

print(bcolors.OKGREEN + '--------- INSTALLATION DONE WITH SUCCESS ---------' + bcolors.ENDC)
print(bcolors.OKBLUE + '*******************************************************' + bcolors.ENDC)
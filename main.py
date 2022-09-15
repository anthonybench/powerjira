#!/usr/bin/env python3
#===================================
# PowerJira
#   - Isaac Yep
# 
# GitHub:
#   anthonybench
# PyPi:
#   sleepyboy
#===================================
mainDocString = '''
A tool to increase agility with Jira, diminishing the need to open the web-app.
'''

#---Dependencies---------------
# stdlib
from os import uname
from sys import argv, exit
# custom modules
from toolchain.option_utils import usageMessage, checkListOverlap, verifyOption
# 3rd party
try:
  from powerjira import fetchIssue, createTicket
except ModuleNotFoundError as e:
  print("Error: Missing one or more 3rd-party packages (pip install).")
  exit(1)

#---Parameters-----------------
userArgs = argv[1:]
minArgs  = 0
maxArgs  = 2
options  = {
  'help'   : ['-h', '--help'],
  'fetch'  : ['--fetch=', 'str'],
  'raw'    : ['-r', '--raw'],
}

#---Entry----------------------
def main():
  ## Invalid number of args
  if len(userArgs) < (minArgs) or len(userArgs) > (maxArgs):
    usageMessage(f"Invalid number of options in: {userArgs}\nPlease read usage.")
    exit(1)
  ## Invalid option
  if (len(userArgs) != 0) and not (verifyOption(userArgs, options)):
    usageMessage(f"Invalid option(s) entered in: {userArgs}\nPlease read usage.")
    exit(1)
  ## Help option
  if checkListOverlap(userArgs, options['help']):
    print(mainDocString, end='')
    usageMessage()
    exit(0)
  else:
    ## Option - Fetch Issue
    if [i for i in userArgs if options['fetch'][0] in i] != []:
      fetchIssue('agent.yml', userArgs)
      exit(0)
    ## Option - Create Ticket
    createTicket('config.yml', 'agent.yml', 'summary', 'description', userArgs)
    exit(0)


#---Exec-----------------------
if __name__ == "__main__":
    main()

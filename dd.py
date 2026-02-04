#
import os

a = input('ENTER ISO IMAGE: ')
b = input('ENTER DESTINATION DISK: ')
c = input(' PRESS ENTER TO EXECUTE DD ')

os.system('dd if=' +a + ' of=' +b + ' status=progress')

d = input('  PRESS ENTER TO EXIT PROGRAM')
####


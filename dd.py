#
import os

a = input('ENTER DISK IMAGE: ')
b = input('ENTER DESTINATION DISK: ')
c = input(' PRESS RETURN TO EXECUTE DD ')

os.system('dd if=' +a + ' of=' +b + ' status=progress')

d = input('  PRESS RETURN TO EXIT PROGRAM')
####


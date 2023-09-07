 #leapyear 

'''
 year % 4==0 &
 year % 100 != 0/
 year % 400 ==0

 '''
def isleapYear(year):
  if(year%4==0 and year%100!=0):
    return True 
  else :
    return False 

year= 2012

if isleapYear(year):
  print("{} is aleapyear".format(year)) 
else:
  print ("{} is not a leapyear".format(year))
  
####################
# CST-205          #
# Module 7 Lab 15  #
# Sevren Gail      #
# Chris Rendall    #
####################

from random import randint
from calendar import weekday

day = 0
month = 0
year = 0

def getRoll(): # returns the result of rolling a 6-sided die
  return randint(1, 6)

def getDoubleRoll(): # returns the result of rolling two 6-sided dice
  return randint(2, 12)

def playCraps(): # simulates craps; gets user input for rolling and loops until user quits
  playAgain = True
  while playAgain:
    raw_input("Let's play craps! Roll when ready (type anything).")
    roll = getDoubleRoll()
    if roll == 7 or roll == 11:
      printSuccess(roll)
    elif roll == 2 or roll == 3 or roll == 12:
      printFailure(roll)
    else:
      raw_input("You got a " + str(roll) + ". Roll again when ready (type anything).")
      while True:
        roll2 = getDoubleRoll()
        if roll == roll2:
          printSuccess(roll2)
          break
        elif roll2 == 7:
          printFailure(roll2)
          break
        raw_input("You got a " + str(roll2) + ". Come on " + str(roll) + "! Roll again when ready (type anything).")
    response = ""
    while not "y" in response and not "n" in response:
      response = str(raw_input("Play again (yes or no)? ")).lower()
    if not "y" in response:
      playAgain = False

def printSuccess(roll): # prints a success message when user wins
  printNow("You rolled a " + str(roll) + ". Great job! You won!")

def printFailure(roll): # prints a failure message when user loses
  printNow("You rolled a " + str(roll) + ". Bummer! You just lost!")

def getNumber(name, start, end): # prompts user for a number with given name between start & end
  response = ""
  while response == "":
    response = raw_input("Input the " + str(name) + ": ")
    if int(response) < start or int(response) > end:
      printNow("Bad value! Try again.")
      response = ""
  return response

def getDayCount(month, year): # returns the number of days in the given month of the given year
  dayCount = 28
  if month == 2:
    if year % 4 == 0 and not year % 100 == 0:
      dayCount = 29
  elif month == 1 or month == 3 or month == 5 or month == 6 or month == 8 or month == 10 or month == 12:
    dayCount = 31
  else:
    dayCount = 30
  return dayCount

def getDate(): # prompts user for a date, testing values and filling global variables
  global day
  global month
  global year
  month = int(getNumber("month as a number", 1, 12))
  year = int(getNumber("year", -10000, 10000))
  day = int(getNumber("day", 1, getDayCount(month, year)))

def getWeekday(month, day, year): # returns the weekday name of the given date
  days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  return days[weekday(year, month, day)]

def getWeekdayNumber(month, day, year): # returns the weekday number of the given date
  return weekday(year, month, day)

def printBirthMonth(): # prompts user for birthdate & prints a calendar of that month
  global year
  global month
  months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
  printNow("Enter your birthdate.")
  getDate()
  printNow("\n               " + months[month - 1] + " " + str(year))
  emptyDays = getWeekdayNumber(month, 1, year)
  if emptyDays == 6:
    emptyDays = 0
  else:
    emptyDays += 1
  dayCount = getDayCount(month, year)
  calendar = "Su   Mo   Tu   We   Th   Fr   Sa\n"
  day = 0
  counter = 0
  while day < dayCount:
    counter += 1
    if emptyDays > 0:
      calendar += "       "
      emptyDays -= 1
    elif day <= dayCount:
      day += 1
      calendar += str(day) + "   "
      if len(str(day)) == 1:
        calendar += "  "
    else:
      break
    if counter == 7:
      calendar += "\n"
      counter = 0
  printNow(calendar)

def getDoIweekday(): # returns the weekday of the signing of the Declaration of Independence
  return getWeekday(7, 4, 1776)

#playCraps()
#printBirthMonth()
printNow(getDoIweekday())
# Class diary
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
#
# Please, use your imagination and create more functionalities.
# Your project should be able to handle entire school(s?).
# If you have enough courage and time, try storing (reading/writing)
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface (might be text-like).
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#
#Delete these comments before commit!
#Good luck.

from dataclasses import dataclass
import datetime


@dataclass
class Grade:
  grade: float
  course: str
  grade_date: datetime

  def __init__(self, grade, course, grade_date):
    self.grade = grade
    self.course = course
    self.grade_date = grade_date



class Student:

  def __init__(self, name, surname):
    self.name = name
    self.surname = surname
    self.grades = list()

  def new_grade(self, course, grade, grade_date):
    new_grade = Grade(grade, course, grade_date)
    self.grades.append(new_grade)

  def average_course_grades(self, course):
    #no time to make it for special one course
    average = 0.0
    for i in self.grades:
      average += self.grades[i].grade
    return average/len(self.grades)


if __name__ == "__main__":

  student = Student("Jan", "Kowalski")
  today_date = datetime.datetime(2020, 11, 9)
  student.new_grade("PitE", 3.0, today_date)
  print("New grade {} for student {} {} at {}".format(3.0, student.name, student.surname, today_date.strftime("%x")))

  print("Student average grade: {} ".format(student.average_course_grades))


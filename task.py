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
from statistics import mean
import datetime
import random


@dataclass
class Grade:
  grade: float
  course: str
  grade_date: datetime


class Student:

  def __init__(self, name):
    self.name = name
    self.grades = list()

  def new_grade(self, course, grade, grade_date):
    new_grade = Grade(grade, course, grade_date)
    self.grades.append(new_grade)

  def average_course_grades(self, course):
    if not self.grades:
      return 0 
    filtered_grades = [g.grade for g in self.grades]
    print(filtered_grades)
    return mean(filtered_grades)


if __name__ == "__main__":

  random.seed(a=None, version = 2)
  file = open("names.txt", "r")
  students = list() 

  for i in range(12):
    student_name = file.readline()
    student = Student(student_name)
    students.append(student)

  courses = ["PitE", "C course", "Physics"]
  grades = [2.0, 3.0, 3.5, 4.0, 4.5, 5.0]
  today_date = datetime.datetime(2020, 11, 23)

  for i in range(20):
    course = courses[random.randrange(2)]
    grade = grades[random.randrange(5)]
    student_index = random.randrange(11)
    students[student_index].new_grade(course, grade, today_date)
    print("New grade {} for student {} for course {}".format(grade, students[student_index].name, course))

  print("Student average grade: {} for PitE".format(students[0].average_course_grades("PitE")))


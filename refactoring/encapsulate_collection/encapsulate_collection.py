
import copy
# old_data
class person(object):
    def __init__(self):
        self.courses = []
    def get_courses(self):
        return self.courses
    def set_courses(self,courses):
        self.courses = courses


# new data
class new_person(object):
    def __init__(self):
        self.courses = []
    def get_courses(self):
        courses = copy.deepcopy(self.courses)
        return courses
    def add_courses(self,course):
        self.courses.append(course)
    def remove_courses(self,remove_course):
        for course in self.courses:
            if course == remove_course:
                self.courses.remove(course)

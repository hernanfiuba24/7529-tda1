import sys, datetime, itertools
import pdb
from Queue import *

def initialize(parameters_max, students_with_ordered_priors, hospitales_with_priors, hospital_reduction):
    path = sys.argv[1]
    with open(path, 'r') as f:
        lines_file = f.readlines()
        max_alumnos = int(lines_file[0])
        i = 1
        while (i < max_alumnos + 1):
            a_student_line = lines_file[i]
            a_student = a_student_line.split(" ")
            a_student = map(int, a_student)
            a_student_indexes = sorted(range(len(a_student)), key=lambda k:a_student[k], reverse=True)
            students_with_ordered_priors.append(a_student_indexes)
            i += 1

        max_hospitals = int(lines_file[i])
        vacant_per_hospital_line = lines_file[max_alumnos + max_hospitals + 2]
        vacant_per_hospital = vacant_per_hospital_line.split(" ")
        vacant_per_hospital = map(int, vacant_per_hospital)
        ##print "Vacants per hospital:\n", vacant_per_hospital
        i += 1
        hospital = 0
        while (i < len(lines_file) - 1):
            if (hospital < max_hospitals and vacant_per_hospital[hospital] > 0):
                a_hospital_line = lines_file[i]
                a_hospital = a_hospital_line.split(" ")
                a_hospital = map(int, a_hospital)
                a_hospital_indexes = sorted(range(len(a_hospital)), key=lambda k:a_hospital[k], reverse=True)
                #print " prior hospital i :", a_hospital_indexes
                for k in xrange(vacant_per_hospital[hospital]):
                    hospital_reduction.append(hospital) 
                    ##print 'hospital_' + str(hospital) + '-q_' + str(k)
                    hospitales_with_priors.append(a_hospital)
            i += 1
            hospital +=1
        parameters_max['max_students'] = max_alumnos
        parameters_max['max_hospitals'] = max_hospitals

def pref(hospitales_with_priors, student, rival_student, hospital):

    student_preference = hospitales_with_priors[hospital][student]
    rival_student_preference = hospitales_with_priors[hospital][actual_student_wanted_by_hospital]
    return student_preference > rival_student_preference


if __name__ == "__main__":
    FORMAT = '%H:%M:%S'
    startTime = datetime.datetime.now().strftime(FORMAT);
    max_alumnos = -1
    max_hospitals = -1
    parameters_max = {'max_students':-1, 'max_hospitals':-1}
    # Per each student have a ordered hospital priors list 
    students_with_ordered_priors = []
    # Variable to keep a reference from student ->  hospital prior
    #students_indexes = []
    # Per each hospital have a ordered student priors list 
    hospitales_with_priors = []
    # Variable to keep a reference from hospital ->  student prior
    #hospital_indexes = []

    #Reference to the real hospitals
    hospital_reduction = []
    initialize(parameters_max, students_with_ordered_priors, hospitales_with_priors, hospital_reduction)
    
    ##print "hospital equivalent for reduction: \n", hospital_reduction
    ##print "cantidad de estudiantes : ", parameters_max['max_students']
    ##print "students with ordered priors (represent the index of hospital)\n", students_with_ordered_priors        
    ##print "cantidad de hospitales : ", parameters_max['max_hospitals']
    ##print "hospitales with desorden priors (represent the index of student)\n", hospitales_with_priors


    # Matches -> hospital que matchea con estudiante 
    student_which_matches_to_hospital = [None] * int(parameters_max['max_hospitals'])
    ##print "\nstudents's matches:\n", student_which_matches_to_hospital
    # Estudiantes los cuales aun no matchean con nadie
    student_pending = Queue(range(int(parameters_max['max_hospitals'])))
    for i in range(int(parameters_max['max_hospitals'])):
        student_pending.put(i)
    # Hospital que desean matchear los estudiantes(index)
    students_wanted_to_hospital_index = [0] * int(parameters_max['max_hospitals'])
    ##print "actual students preferences index hospital :\n", students_wanted_to_hospital_index
    ##print
    max_round = student_pending.qsize()
    nro_round = 1
    index_round = 1 
    ##print "******** ROUND", nro_round,"********"
    ##print "MAX ROUND : ", max_round 


    while (not(student_pending.empty())):
        #pdb.set_trace()
        student = student_pending.get()
        #print "student's name is: ", student
        hospital_index_wanted_by_student = students_wanted_to_hospital_index[student]
        #print "student", student, " wanted to hospital index: ", hospital_index_wanted_by_student
        hospital_wanted_by_student = students_with_ordered_priors[student][hospital_index_wanted_by_student]
        #print "hospital's name wanted by student", student, " is : ", hospital_wanted_by_student
        actual_student_wanted_by_hospital = student_which_matches_to_hospital[hospital_wanted_by_student]
        #print "actual student name : ", actual_student_wanted_by_hospital, " matching by hospital", hospital_wanted_by_student
        if (actual_student_wanted_by_hospital is None):
            #print
            #print "actual hospital name", hospital_wanted_by_student, " is NONE"
            #print
            student_which_matches_to_hospital[hospital_wanted_by_student] = student
        elif pref(hospitales_with_priors, student, actual_student_wanted_by_hospital, hospital_wanted_by_student):
            #print
            #print "actual hospital name", hospital_wanted_by_student, " have student name ", student, " with GREATER prior than student name ", actual_student_wanted_by_hospital
            #print
            student_which_matches_to_hospital[hospital_wanted_by_student] = student 
            student_pending.put(actual_student_wanted_by_hospital)
            students_wanted_to_hospital_index[actual_student_wanted_by_hospital] += 1;
        else:
            #print
            #print "actual hospital name", hospital_wanted_by_student, " have student name ", student, " with LESS prior than student name ", actual_student_wanted_by_hospital
            #print
            student_pending.put(student)
            students_wanted_to_hospital_index[student] += 1;
        #print "hospitals' matches: ", student_which_matches_to_hospital
        if (index_round == max_round):
            max_round = student_pending.qsize()
            index_round = 1
            if (max_round > 0):
                ##print
                nro_round += 1
                ##print "******** ROUND", nro_round,"********"
                ##print "MAX ROUND : ", max_round
        else:
             index_round += 1 
        ##print "actual students preferences index : ", students_wanted_to_hospital_index
        ##print
        ##print

    
    ##print student_which_matches_to_hospital 
    
    for student in student_which_matches_to_hospital:
        hospital_match_to_student = student_which_matches_to_hospital[student]
        print "student",student, "match to hospital", hospital_reduction[hospital_match_to_student]
    
    finishTime = datetime.datetime.now().strftime(FORMAT);
    deltaTime = datetime.datetime.strptime(finishTime, FORMAT) - datetime.datetime.strptime(startTime, FORMAT)
    print "Time of executing is " + str(deltaTime)


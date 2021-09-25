from codeitsuisse.routes.parasite_1 import parasiteP1
from codeitsuisse.routes.parasite_2 import parasiteP2
from codeitsuisse.routes.parasite_3 import parasiteP3
from codeitsuisse.routes.parasite_4 import parasiteP4


def solveProblem1(room):
    question1ans={}
    for people in room['interestedIndividuals']:
        question1ans[people]=int(parasiteP1(room['grid'],people))
    return question1ans

def solveProblem2(room):
    return int(parasiteP2(room['grid']))

def solveProblem3(room):
    return int(parasiteP3(room['grid']))

def solveProblem4(room):
    return int(parasiteP4(room['grid']))

def solve_All(room):
    ans_of_room={}
    ans_of_room['room']=room['room']
    ans_of_room['p1']=solveProblem1(room)
    ans_of_room['p2']=solveProblem2(room)
    ans_of_room['p3']=solveProblem3(room)
    ans_of_room['p4']=solveProblem4(room)
    return  ans_of_room



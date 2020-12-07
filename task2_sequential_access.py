import pickle
from university_record import University




# This function will sort all University objects by rank
# then save them to a binary file data_task2.bin using pickle
# The file should only store 5 universities at a time
def sort_and_save_universities(universities_array):


    ##############################
    # Write your code to sort then
    # save the binary data here
    ##############################


    n = len(universities_array) - 1
    while True:
        No_more = True
        for i in range(n):
            if universities_array[i].world_rank > universities_array[i+1].world_rank:
                temp = universities_array[i]
                universities_array[i] = universities_array[i+1]
                universities_array[i+1] = temp
                No_more = False
        n = n-1
        if No_more == True:
            break



    file = open("data_task2.bin", "wb")

    for uni in universities_array:
        pickle.dump(uni, file)

    file.close()






# This function will read data_task2.bin and return
# an array of the top 5 world universities stored
def get_top_5_universities():
    top_universities = []
    ##########################
    file = open("data_task2.bin", "rb")

    while True:
        try:
            top_universities.append(pickle.load(file))
        except EOFError:
            break

    file.close()





    ##########################

    for university in top_universities:
        print("Rank:", university.world_rank, end=" ")
        print(university.name, "(", university.country, ")")

    return top_universities






# Functions that include the correct university ranking data.
# Please do no change anything below this line!
# Do not edit me!
def save_top_5_universities_2019():
    caltech = University("California Institute of Technology", "USA", 5)
    cambridge = University("University of Cambridge", "UK", 2)
    mit = University("Massachusetts Institute of Technology", "USA", 4)
    oxford = University("University of Oxford", "UK", 1)
    stanford = University("Stanford University", "USA", 3)

    sort_and_save_universities([caltech, cambridge, mit, oxford, stanford])


# Do not edit me!
def save_top_5_universities_2020():
    caltech = University("California Institute of Technology", "USA", 2)
    cambridge = University("University of Cambridge", "UK", 3)
    mit = University("Massachusetts Institute of Technology", "USA", 5)
    oxford = University("University of Oxford", "UK", 1)
    stanford = University("Stanford University", "USA", 4)

    sort_and_save_universities([caltech, cambridge, mit, oxford, stanford])


# Do not edit me!
def save_top_5_universities_2021():
    caltech = University("California Institute of Technology", "USA", 2)
    harvard = University("Harvard University", "USA", 3)
    mit = University("Massachusetts Institute of Technology", "USA", 5)
    oxford = University("University of Oxford", "UK", 1)
    stanford = University("Stanford University", "USA", 2)

    sort_and_save_universities([caltech, harvard, mit, oxford, stanford])

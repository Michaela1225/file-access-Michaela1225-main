# Reads the serial text file 'data_task1.txt' and returns the number of students who left campus for lunch today
def count_off_campus_students():
    file = open("data_task1.txt", "r")
    exit_count = 0

    for line in file.readlines():
        for word in line.split():
            if word == "exit,":
                exit_count = exit_count + 1
    file.close()
    return exit_count


# Reads the serial text file 'data_task1.txt' and returns a list of students who
# checked in to campus (entry) at 13:35 or after
def late_students():
    file = open("data_task1.txt", "r")
    people = []

    for line in file.readlines():
        for section in line.split(", "):
            if section[0] == "1" and section[1] == "3":
                if int(section[3]) >= 3 and int(section[4]) >= 5:
                    late = line.split(", ")[0]
                    people.append(late)
    return people


# Reads the serial text file 'data_task1.txt' and returns a list of students who
# checked out of campus (exit) but did not return for afternoon class (entry)
def missing_students():
    file = open("data_task1.txt", "r")
    exited = []
    enter = []
    left = []
    for line in file.readlines():
        section = line.split(", ")
        if section[1] == "exit":
            exited.append(section[0])
        if section[1] == "entry":
            enter.append(section[0])

    for i in range(len(exited)):
        if exited[i] not in enter:
            left.append(exited[i])
        else:
            pass

    return left

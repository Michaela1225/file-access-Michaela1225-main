import pickle
from student_record import Student

# Assign 120 bytes for each student username record
RECORD_SIZE = 120


# Receives a single student username and returns an integer
# Each hash created should be unique
# Ideally, it will be a multiple of 60 as each record is up to 30 bytes in size
# There are 21 records total, a perfect situation would be hashes of 0, 120, 240, etc...
def student_username_hash(username):
    # Complete your hash function here!!

    student_text_file = open("data_task3_student_list.txt", "r")
    array = student_text_file.read().split('\n')
    student_text_file.close()
    num = array.index(username)


    return num*240


def write_single_student_record(student):
    # Open the student data file in read and write mode
    student_data_file = open("data_task3.bin", "rb+")

    # Find the correct memory location using the hash function
    hash_address = student_username_hash(student.username)

    # Move the file pointer to the correct address
    student_data_file.seek(hash_address, 0)

    # Write a single student object to the appropriate memory location
    pickle.dump(student, student_data_file)

    student_data_file.close()


def read_single_student_record(username):
    # Open the student data file in read and write mode
    student_data = open("data_task3.bin", "rb")

    # Find the correct memory location using the hash function
    hash_address = student_username_hash(username)

    # Move the file pointer to the correct address
    student_data.seek(hash_address, 0)


    # Load a single student object to the appropriate memory location
    return pickle.load(student_data)

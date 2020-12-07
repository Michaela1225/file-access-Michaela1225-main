from task3_random_access import *
from student_record import Student


def student_record_type():
    test_student = Student("test.student")
    print(type(test_student).__name__)


def load_all_student_usernames():
    student_text_file = open("data_task3_student_list.txt", "r")
    usernames = student_text_file.read().split('\n')
    student_text_file.close()
    return usernames


def test_load_all_usernames():
    usernames = load_all_student_usernames()
    assert len(usernames) == 21
    assert usernames[0] == "Jack.Chen21"
    assert usernames[20] == "Andy.Zhu21"


def test_binary_writing():
    ml = Student("Michaela.Liu21")
    dm = Student("Dongming.Piao21")
    test_bin = open("data_task3_largest_username.bin", "wb")
    pickle.dump(ml, test_bin)
    pickle.dump(dm, test_bin)
    test_bin.close()


def test_for_unique_hashes():
    usernames = load_all_student_usernames()
    hashes_set = set([])

    for username in usernames:
        hashes_set.add(student_username_hash(username))

    assert len(usernames) == len(hashes_set)


def test_writing_all_students():
    usernames = load_all_student_usernames()

    for username in usernames:
        student = Student(username)
        write_single_student_record(student)

    student_data = read_single_student_record("Dongming.Piao21")

    assert student_data.username == "Dongming.Piao21"
    assert student_data.year_group == "Y13"
    assert type(student_data).__name__ == "Student"

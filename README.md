# Y13 File Access Exercises
Practice Python exercises for working with data serially, sequentially and randomly

## Task 1 - Serial access of a text file
Y13 students at DHSZ are allowed to leave campus during the lunch break. The school wants to start recording the entry
and exit time of students each day. The school decides to write a Python program to achieve this and store data for each
student entering and leaving campus serially.

A sample of the data file is as follows:
```
Jack Chen (13S1-LH), exit, 12:41
Charles Ji (13F3-JRA), exit, 12:42
Jack Jia (13S2-KA), exit, 12:42
Finn Li (13R1-XJ), exit, 12:43

...

Connie Zhou (13S1-LH), entry, 13:28
Frank Zhou (13S2-KA), entry, 13:35
Jacob Zhou (13G3-JC), entry, 13:36
Andy Zhu (13G2-SZE), entry, 13:37
```

Complete the file `task1_serial_access.py` and complete the following functions:
- `count_off_campus_students()` - this should return the number of students who left campus for lunch as an integer
- `late_students()` - this should return a list of students who returned to campus after 13:35 making them late for 
afternoon classes
- `missing_students()` - this should return a list of students who left for lunch but did not return for 
afternoon classes


## Task 2 - Sequential access using a binary file
Every year an organisation known as TES releases their list of worldwide university rankings.

We have written a program to store the current top 5 universities using a binary file. As this data only needs to be changed
once per year, we have opted to store the universities in a sequential file using each university's rank for that year
as the order for storing the data.

You need to complete the implementation of the following 2 functions in the `task2_sequential_access.py` file:
- `sort_and_save_universities(universities_array)` - this function receives an array of `University` objects, but they are not
yet in order. Sort the university array by rank and then save the data as a binary file `data_task2.bin` using `pickle`.
- `get_top_5_universities()` - this function will read the binary file `data_task2.bin` and return the top 5 worldwide
universities as `University` objects.

## Task 3 - Random access using a binary file
We have been tasked with implementing a method of storing student data randomly in a binary file.

Each student is stored as an object called `Student` which contains the attributes `username` and `year_group`.

Your task is to complete the implementation of a hashing function to decide at what address in the binary file each 
record should be stored.

- `student_username_hash(username)`: Will receive a username as a string and return a unique integer based on the input.
The hash function should return the same value every time is is called with the same input.

import pickle
from university_record import University
from task2_sequential_access import *


def test_2019_universities():
    save_top_5_universities_2019()
    top5_2019 = get_top_5_universities()
    assert top5_2019[0].name == "University of Oxford"
    assert top5_2019[0].country == "UK"
    assert top5_2019[0].world_rank == 1


def test_2020_universities():
    oxford = University("University of Oxford", "UK", 1)
    caltech = University("California Institute of Technology", "USA", 2)
    cambridge = University("University of Cambridge", "UK", 3)
    stanford = University("Stanford University", "USA", 4)
    mit = University("Massachusetts Institute of Technology", "USA", 5)
    save_top_5_universities_2020()
    top5_2020 = get_top_5_universities()
    top5_test_data = [oxford, caltech, cambridge, stanford, mit]
    for x in range(len(top5_2020)):
        assert top5_2020[x].name == top5_test_data[x].name


def test_2021_universities():
    mit = University("Massachusetts Institute of Technology", "USA", 5)
    save_top_5_universities_2021()
    top5_2021 = get_top_5_universities()
    assert top5_2021[4].name == mit.name
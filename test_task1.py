from task1_serial_access import *


def test_count_off_campus_students():
    assert count_off_campus_students() == 21


def test_late_students():
    assert late_students() == ["Frank Zhou (13S2-KA)", "Jacob Zhou (13G3-JC)", "Andy Zhu (13G2-SZE)"]


def test_missing_students():
    assert missing_students() == ["Jack Chen (13S1-LH)", "Carl Dong (13F3-JRA)", "Brian Tan (13F4-SS)", "Frank Wang (13G4-BT)"]
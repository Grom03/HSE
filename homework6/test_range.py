import pytest
from range import Range

def range_equals(range1: Range, range2: Range):
    return range1.equals(range2)

def test_init():
    range = Range()
    range = Range(1, 2)

def test_get_min():
    range = Range()
    assert range.get_min() is None
    range = Range(1, 2)
    assert range.get_min() == 1

def test_get_max():
    range = Range()
    assert range.get_max() is None
    range = Range(1, 2)
    assert range.get_max() == 2

def test_intersection_good():
    range1 = Range(1, 5)
    range2 = Range(3, 7)
    assert range_equals(range1.intersection(range2), Range(3, 5))

def test_intersection_bad():
    range1 = Range(1, 5)
    range2 = Range(6, 7)
    range3 = Range()
    assert range_equals(range1.intersection(range2), range3)
    assert range_equals(range1.intersection(range3), range3)
    assert range_equals(range3.intersection(range1), range3)

def test_unify_crossing_intervals():
    range1 = Range(1, 5)
    range2 = Range(3, 7)
    assert range_equals(range1.unify_crossing(range2), Range(1, 7))

def test_unify_not_crossing_or_empty_intervals():
    range1 = Range(1, 5)
    range2 = Range(6, 7)
    range3 = Range()
    assert range_equals(range1.unify_crossing(range2), range3)
    assert range_equals(range1.unify_crossing(range3), range3)
    assert range_equals(range3.unify_crossing(range1), range3)

def test_empty_interval():
    range1 = Range(6, 7)
    range2 = Range()
    assert not range1.empty_interval()
    assert range2.empty_interval()

def test_point_in_interval():
    range1 = Range(2, 5)
    range2 = Range()
    assert range1.is_point_inside(3)
    assert not range1.is_point_inside(1)
    assert not range1.is_point_inside(6)
    assert not range1.is_point_inside(None)
    assert not range2.is_point_inside(1)

def test_crossing():
    range1 = Range(1, 5)
    range2 = Range(6, 7)
    range3 = Range()
    range4 = Range(3, 6)
    assert not range1.crossing(range2)
    assert not range1.crossing(range3)
    assert range1.crossing(range4)
    assert range2.crossing(range4)

def test_is_inside():
    range1 = Range(1, 7)
    range2 = Range(2, 7)
    range3 = Range()
    range4 = Range(2, 7)
    assert range1.is_inside(range2)
    assert not range1.is_inside(range3)
    assert not range3.is_inside(range1)
    assert not range2.is_inside(range1)
    assert range2.is_inside(range4)
    assert range4.is_inside(range2)

def test_view_points():
    range1 = Range(1, 5)
    assert range1.view_points() == [1, 2, 3, 4, 5]
    range2 = Range()
    assert range2.view_points() == []

def test_out_interval():
    range1 = Range(1, 5)
    range2 = Range()
    assert range1.out() == '[1, 5]'
    assert range2.out() == '[]'

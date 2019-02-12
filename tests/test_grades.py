from grades import average


def test_avg():
    marks = {'somu': [90, 100], 'bob': [100]}
    ans = {'somu': 95.0, 'bob': 100.0}
    assert average(marks) == ans

from grades import average, readfile


def test_avg():
    marks = {'somu': [90, 100], 'bob': [100]}
    ans = {'somu': 95.0, 'bob': 100.0}
    assert average(marks) == ans


def test_readfile():
    ans = readfile('grades.txt')
    a_test = {}
    len(ans) == 3
    isinstance(ans, type(a_test))

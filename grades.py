# read in grades.txt
# print out a list of students
# and their avg grade for class
# and rank them in order
# from high to low
# i.e., bob 98, sue 97, sara 76


def average(mark_dict):
    avg = {}
    for key in mark_dict:
        marks = mark_dict[key]
        avg[key] = sum(marks) / len(marks)
    return avg


mark = {}
with open('grades.txt') as f:
    for line in f:
        a, b = line.strip().split(' ')
        if a in mark:
            mark[a].append(float(b))
        else:
            mark[a] = [float(b)]

result = average(mark)
print(sorted(result.items(), key=lambda kv: kv[1],
             reverse=True))

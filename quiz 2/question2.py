def make_schedule(period1, period2):
    schedule = ("[1st]" + period1.title() + ",[2nd]" + period2.title())
    return schedule


student_schedule = make_schedule("Javascript", "Python")
print("SCHEDULE:", student_schedule)

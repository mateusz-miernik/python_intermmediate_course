from datetime import datetime


def create_function(span='m'):
    if span == 'm':
        sec = 60
    elif span == 'h':
        sec = 3600
    elif span == 'd':
        sec = 86400

    source = """
def f(start, end):
    duration = end - start
    duration_in_sec = duration.total_seconds()
    result = divmod(duration_in_sec, {})[0]
    return result
    """.format(sec)

    exec(source, globals())

    return f


start = datetime(2019, 1, 1, 0, 0, 0)
end = datetime.now()
f_minutes = create_function('m')
f_hours = create_function('h')
f_days = create_function('d')
print(f_minutes(start, end))
print(f_hours(start, end))
print(f_days(start, end))
import os


def calculate_paint(efficiency_ltr_per_m2, *args):
    for arg in args:
        if isinstance(arg, list) is not True:
            result = efficiency_ltr_per_m2 * arg
            print(f"For efficiency {efficiency_ltr_per_m2} and surface {arg} you need {result} litres of paint.")
        else:
            for item in arg:
                result = efficiency_ltr_per_m2 * item
                print(f"For efficiency {efficiency_ltr_per_m2} and surface {item} you need {result} litres of paint.")


def log_it(*args):
    result = ''
    with open('write_arguments.txt', 'a+') as f:
        for arg in args:
            if isinstance(arg, list) is not True:
                result += arg + ' '
            else:
                for item in arg:
                    result += item + ' '
        f.write(result)
        f.write('\n')


# calculate_paint(0.33, 34, 54, 67, 89)
rooms = [11, 45, 68, 75]
calculate_paint(0.33, *rooms)

log_it('event1', 'event1', 'event3')
log_it('event4')
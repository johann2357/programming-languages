###
# Integrantes
# Johann Nunez Garcia
# Jeffrey Aguirre Corrales
###


from pprint import pprint
from datetime import time, datetime, date, timedelta

days = [
    'mon',
    'tue',
    'wed',
    'thu',
    'fri',
    'sat',
    'sun',
]


def get_times(p):
    """
        Get the times in the following format
        [(desde, hasta), (desde, hasta), ....]
    """
    result = []
    for pair in p:
        pair = pair.split('-')
        from_ = pair[0].split(':')
        to_ = pair[1].split(':')
        result.append((
            time(int(from_[0]), int(from_[1])),
            time(int(to_[0]), int(to_[1])),
        ))
    return result


def read_file(f):
    """
        Just open the file and get the respective dict
        { 'day' : [(desde, hasta), (desde, hasta), ....] }
    """
    d = {}
    with open(f) as schedule:
        for line in schedule:
            day = line.split()
            d[day[0]] = get_times(day[1:])
    return d


def get_schedule(range_, time_):
    # FIXME: this function should determine the schedule considering how long
    #        the reunion should be
    return
    start = range_[0][0]
    finish = range_[0][1]
    new_schedule = []
    new_time = ()
    for from_, to_ in range_[1:]:
        time_free = (
            datetime.combine(
                date.today(),
                finish
            ) - datetime.combine(date.today(), from_)
        )
        finish = from_
        if time_free >= time_:
            new_time = (start, to_)
            new_schedule.append(new_time)
            start = from_
        else:
            start = from_
    return new_schedule


def print_schedule(final_schedule):
    """
        It should print the result with the format as follow:
         > mon 14:35-16:00 17:10-17:58
         > tue 13:31-15:13
    """
    pass


def merge_schedules(schedules):
    """
        Function that get the merged schedule of availability
        Returns a dict with the respectives days and a list of tuples
        of the beginning end time of the period
    """
    day_availability = dict()
    for d in days:
        day_schedule = []
        for sch in schedules:
            day_schedule.append(sch.get(d, []))

        day_availability[d] = []
        for pivot in day_schedule[0]:
            for p in day_schedule[1:]:
                for tp in p:
                    if pivot[1] > tp[0]:
                        beginning = max(pivot[0], tp[0])
                        end = min(pivot[1], tp[1])
                        if beginning < end:
                            day_availability[d].append((beginning, end))
    return day_availability


def main():
    s = raw_input('ingrese parametros:')
    p = s.split()
    reunion = p[0].split(':')
    schedules = []
    for f in p[1:]:
        schedules.append(read_file(f))
    reunion = timedelta(hours=int(reunion[0]), minutes=int(reunion[1]))
    general_schedule = merge_schedules(schedules)
    # TODO: delete this print and test all the possible cases
    pprint(general_schedule)
    # TODO: make this work
    print_schedule(
        get_schedule(general_schedule, reunion)
    )

    return

    # FIXME: this still could be useful if not please deleted
    # for x in schedules:
    #     for k, v in x.iteritems():
    #         print k, ' ---> ',
    #         v = get_schedule(v, reunion)
    #         for from_, to_ in v:
    #             print ' %d:%d-' % (from_.hour, from_.minute),
    #             print '%d:%d ' % (to_.hour, to_.minute),


main()

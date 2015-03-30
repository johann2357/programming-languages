###
# Integrantes
# Johann Nunez Garcia
# Jeffrey Aguirre Corrales
###


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


def read_file(file):
    """
        Just open the file and get the respective dict
        { 'day' : [(desde, hasta), (desde, hasta), ....] }
    """
    d = {}
    with open(file) as schedule:
        for line in schedule:
            day = line.split()
            d[day[0]] = get_times(day[1:])
    return d


def get_schedule(free_sched, time_):
    result = dict()
    for day, sched in free_sched.iteritems():
        if sched:
            for beg, end in sched:
                time_free = (
                    datetime.combine(
                        date.today(),
                        end
                    ) - datetime.combine(date.today(), beg)
                )
                if time_free >= time_:
                    if result.get(day) is None:
                        result[day] = []
                    result[day].append((beg, end))
    return result


def print_schedule(final_schedule):
    """
        It should print the result with the format as follow:
         > mon 14:35-16:00 17:10-17:58
         > tue 13:31-15:13
    """
    for day, sched in final_schedule.iteritems():
        print '%s' % day,
        for beg, end in sched:
            print ' %i:%i-%i:%i' % (
                beg.hour, beg.minute,
                end.hour, end.minute,
            ),
        print


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

        # start_hour is the hour of start
        # of the first schedule in the first day of the week
        # start_hour = day_schedule[0][0][0].hour
        # for f_fil in day_schedule:
        #     for f_col in f_fil:
        #         for f_s, f_f in f_col:
        #             for fil in day_schedule:
        #                 for col in fil:
        #                     for s, f in col:
        #                         if start_hour > s:
        #                             pass

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
    # # TODO: delete this print and test all the possible cases
    # # TODO: make this work
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

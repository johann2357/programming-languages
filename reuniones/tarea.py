###
# Integrantes
# Johann Nunez Garcia
# Jeffrey Aguirre Corrales
###


from datetime import time, datetime, date, timedelta


def get_times(p):
    # [(desde, hasta), (desde, hasta), ....]
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
    d = {}
    with open(f) as schedule:
        for line in schedule:
            day = line.split()
            d[day[0]] = get_times(day[1:])
    return d


def get_schedule(range_, time_):
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


def main():
    s = raw_input('ingrese parametros:')
    p = s.split()
    reunion = p[0].split(':')
    schedules = []
    for f in p[1:]:
        schedules.append(read_file(f))
    reunion = timedelta(hours=int(reunion[0]), minutes=int(reunion[1]))
    for x in schedules:
        for k, v in x.iteritems():
            print k, ' ---> ',
            v = get_schedule(v, reunion)
            for from_, to_ in v:
                print ' %d:%d-' % (from_.hour, from_.minute),
                print '%d:%d ' % (to_.hour, to_.minute),


main()

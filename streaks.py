"""Подсчет серий: сколько дней подряд привычка выполнялась."""
import datetime
def current_streak(days,today):
    # идем назад от сегодняшнего дня, пока есть отметки
    s=0
    d=today
    while d.isoformat() in days:
        s+=1
        d=d-datetime.timedelta(days=1)
    return s
def best_streak(days):
    # самая длинная серия за все время
    if len(days)==0: return 0
    dates=sorted(datetime.date.fromisoformat(x) for x in days)
    best=cur=1
    for a,b in zip(dates,dates[1:]):
        if (b-a).days==1:
            cur+=1
            best=max(best,cur)
        else:
            cur=1
    return best

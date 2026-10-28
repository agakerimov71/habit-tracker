"""Подсчет серий: сколько дней подряд привычка выполнялась."""
import datetime


def current_streak(days, today):
    # идем назад от сегодняшнего дня, пока есть отметки
    streak = 0
    day = today
    while day.isoformat() in days:
        streak += 1
        day = day - datetime.timedelta(days=1)
    return streak


def best_streak(days):
    # самая длинная серия за все время
    if len(days) == 0:
        return 0
    dates = sorted(datetime.date.fromisoformat(x) for x in days)
    best = current = 1
    for prev, nxt in zip(dates, dates[1:]):
        if (nxt - prev).days == 1:
            current += 1
            best = max(best, current)
        else:
            current = 1
    return best

import datetime
from storage import load,save
from streaks import current_streak



def add_habit(data,name):
    if name in data :
        return False
    data[name]=[]
    return True
def mark_done(data,name,day=None):
    if day==None:
        day=datetime.date.today().isoformat()
    if day not in data[name]:
        data[name].append(day)
def show(data,today):
    for name,days in data.items():
        print(name.ljust(20),'серия:',current_streak(days,today),'дн.', 'всего отметок:',len(days))

if __name__=='__main__':
    data=load('habits.json')
    add_habit(data,'зарядка')
    add_habit(data,'читать 20 страниц')
    for d in ['2026-10-25','2026-10-26','2026-10-27','2026-10-28']:
        mark_done(data,'зарядка',d)
    mark_done(data,'читать 20 страниц','2026-10-28')
    save('habits.json',data)
    show(data,datetime.date(2026,10,28))

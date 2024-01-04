"""Markdown Calendar Generator for weekly activities """

import calendar
from datetime import datetime
import sys

def create_week(start, end, month, year, team_members):
    mdstr = ""
    colnames = ["Team Member",	"Done", "WIP", "To Do"]

    for i in range(start, end+1):
        mdstr += str(i) + '/' + str(month) + '/' + str(year) + '\n\n'

        mdstr += '|' + '|'.join(colnames) + '|' + '\n'
        mdstr += '|' + '|'.join([':-:\t' for _ in range(len(colnames))]) + '|' + '\n'
        
        for member in team_members:
            mdstr += '|' + member + '|' + '|'.join(['\t' for _ in range(len(colnames))]) + '\n'

        mdstr += '\n'
    return mdstr

def create_calendar(month, year, team_members, nweek):
    mdstr = ""
    
    cal = calendar.Calendar(firstweekday=0)

    weeks = cal.monthdays2calendar(year, month)
    if nweek != 0:
        weeks = [weeks[nweek-1]]
    
    for week in weeks:
        start, end = get_start_end(week)
        mdstr += create_week(start, end, month, year, team_members)
   
    return mdstr

def get_start_end(week):
    start = week[0][0]
    end = week[0][0]
    for day in week:
        # if weekday number is 6 or 7 (saturday or sunday)
        # or is outside of the current month => continue
        if day[1] > 4 or day[0] == 0:
            continue

        if day[0] < start:
            start = day[0]
        
        if day[0] > end:
            end = day[0]
    
    return start, end

def print_calendar(month, year, team_members, nweek=0):
    print(create_calendar(month, year, team_members, nweek))

if __name__ == "__main__":
    argv = sys.argv
    team_members = ["Member1", "Member2", "Member3"]

    if len(argv) == 3:
        month, year = [int(a) for a in argv[1:5]]
        print_calendar(month, year, team_members)
    elif len(argv) == 4:
        month, year, nweek = [int(a) for a in argv[1:5]]
        print_calendar(month, year, team_members, nweek)
    else:
        print('Usage: python mdcal.py [month] [year] [number of week]')
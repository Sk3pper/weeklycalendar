"""Markdown and Html Calendar Generator for weekly activities """

import calendar
from datetime import datetime
import sys

def get_start_end(week):
    start = week[0][0]
    end = week[0][0]
    for day in week:
        # if weekday number is 5 or 6 (saturday or sunday)
        # or is outside of the current month => continue
        if day[1] > 4 or day[0] == 0:
            continue

        if day[0] < start or start == 0:
            start = day[0]
        
        if day[0] > end:
            end = day[0]
    
    return start, end

def create_week_md(start, end, month, year, team_members):
    mdstr = ""
    colnames = ["Team Member",	"Done", "WIP", "To Do"]

    for i in range(start, end+1):
        mdstr += str(i) + '/' + str(month) + '/' + str(year) + '\n\n'

        mdstr += '|' + '|'.join(colnames) + '|' + '\n'
        mdstr += '|' + '|'.join([':-:\t' for _ in range(len(colnames))]) + '|' + '\n'
        
        for member in team_members:
            mdstr += '|' + member + '|' + '|'.join(['\t' for _ in range(len(colnames))]) + '\n'

        mdstr += '\n'
    return mdstr\
    
def create_week_html(start, end, month, year, team_members, output_html):
    colnames = ["Done", "WIP", "To Do"]

    output_html += "\nFrom {start}/{smonth} to {end}/{emonth}\n".format(start=start, smonth=month, end=end, emonth=month)
    output_html += '<table class="no-border">'

    output_html += '<tr class="no-border">'
    for i in range(start, end+1):
        output_html += '<td class="no-border"> \
                <table> \
                    <tr> \
                        <th>{day}/{month}/{year}</th> \
                        <th>{col0}</th>  \
                        <th>{col1}</th> \
                        <th>{col2}</th> \
                    </tr>'.format(day=i, month=month, year=year,
                                  col0=colnames[0], col1=colnames[1], col2=colnames[2])
        
        for member in team_members:
            output_html += '<tr> \
                                <td>{member}</td> \
                                <td></td> \
                                <td></td> \
                                <td></td> \
                            </tr>'.format(member=member)
                
        output_html += '</table> </td>'  

        if (i-start) == 2 :
            output_html += '</tr>'            
            if (end+1-start) > 3:
                output_html += '<tr class="no-border">'
    
    if (end+1-start) > 3:
        output_html += '</tr>'

    output_html += '</table>'
    
    return output_html

def create_calendar(month, year, team_members, output='html'):
    out = ""
    template_html = "<!DOCTYPE html> <html> <head> \
                    <title>Workday Tables - *Month* *Year*</title> \
                    <style> \
                        table, th, td { \
                            border: 1px solid black; \
                        } \
                        .no-border{ \
                            border: 0px solid black; \
                        } \
                    </style> \
                </head> \
                <body> \
                    <h1>Workday - *Month* *Year*</h1>"

    cal = calendar.Calendar(firstweekday=0)
    weeks = cal.monthdays2calendar(year, month)
        
    # replace month, year
    template_html = template_html.replace("*Month*", calendar.month_name[month])
    template_html = template_html.replace("*Year*", str(year))

    if output == 'html':
        out = template_html

    for week in weeks:
        start, end = get_start_end(week)
        if output == "md":
            out += create_week_md(start, end, month, year, team_members)
        elif output == 'html':
            out = create_week_html(start, end, month, year, team_members, out)
    
    if output == 'html':
        out += "</body> </html>"
    return out

def print_calendar(month, year, team_members, output='html'):
    to_print = create_calendar(month, year, team_members, output=output)

    # write out to file
    if output == "md":
        # write file md
        write_to_file(to_print, "md")
    elif output == 'html':
        write_to_file(to_print, "html")

def write_to_file(text, extension):
    file_name = "weeklycalendar.{extension}".format(extension=extension)
    with open(file_name, "w") as file:
        file.write(text)

if __name__ == "__main__":
    argv = sys.argv
    team_members = ["Member1", "Member2", "Member3"]
    
    if len(argv) == 4:
        month, year = [int(a) for a in argv[1:3]]
        output = argv[3]
        print_calendar(month, year, team_members, output)
    else:
        print('Usage: python mdcal.py [month] [year] [html|md]')
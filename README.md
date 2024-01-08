# weeklycalendar

Generate weekly calendar in Markdown and HTML table. Written in Python3.

## Usage

Generate weekly calendar of current month (excluding saturday and sunday days) in md and html format.

Change the name of the members at line 61
``` team_members = ["Member1", "Member2", "Member3"] ```

```sh
$ python weeklycal.py [month] [year] [format]
```

## Examples
```sh
$ python weeklycal.py 1 2024 html
```
![alt text](https://github.com/Sk3pper/weeklymdcal/blob/main/images/html_example.png?raw=true)


```sh
$ python weeklycal.py 1 2024 md  
```
![alt text](https://github.com/Sk3pper/weeklymdcal/blob/main/images/md_example.png?raw=true)

## Run without download the file
For both Linux and Windows
```sh
curl -sL "https://raw.githubusercontent.com/Sk3pper/weeklycalendar/main/weeklycal.py" | python3 - 1 2024 html
```
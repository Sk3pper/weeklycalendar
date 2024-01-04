# weeklymdcal

Generate weekly calendar in Markdown table. Written in Python3.

## Usage

Generate  weekly calendar of current month (excluding saturday and sunday days).

Change the name of the members at line 61
``` team_members = ["Member1", "Member2", "Member3"] ```

```sh
$ python3 mdcal.py 01 2024
1/1/2024

|Team Member|Done|WIP|To Do|
|:-:|:-:|:-:|:-:|
|Member1|||||
|Member2|||||
|Member3|||||

2/1/2024

|Team Member|Done|WIP|To Do|
|:-:|:-:|:-:|:-:|
|Member1|||||
|Member2|||||
|Member3|||||

3/1/2024

|Team Member|Done|WIP|To Do|
|:-:|:-:|:-:|:-:|
|Member1|||||
|Member2|||||
|Member3|||||

..... etc 3/1/2024, 4/1/2024, 5/1/2024.....

8/1/2024

|Team Member|Done|WIP|To Do|
|:-:|:-:|:-:|:-:|
|Member1|||||
|Member2|||||
|Member3|||||

9/1/2024

|Team Member|Done|WIP|To Do|
|:-:|:-:|:-:|:-:|
|Member1|||||
|Member2|||||
|Member3|||||

..... etc 10/1/2024, 11/1/2024, 12/1/2024.....

```

Generate calendar of specified week of the given month:

```sh
$ python3 mdcal.py 01 2024 2
15/1/2024

|Team Member|Done|WIP|To Do|
|:-:|:-:|:-:|:-:|
|Member1|||||
|Member2|||||
|Member3|||||

16/1/2024

|Team Member|Done|WIP|To Do|
|:-:|:-:|:-:|:-:|
|Member1|||||
|Member2|||||
|Member3|||||

17/1/2024

|Team Member|Done|WIP|To Do|
|:-:|:-:|:-:|:-:|
|Member1|||||
|Member2|||||
|Member3|||||

18/1/2024

|Team Member|Done|WIP|To Do|
|:-:|:-:|:-:|:-:|
|Member1|||||
|Member2|||||
|Member3|||||

19/1/2024

|Team Member|Done|WIP|To Do|
|:-:|:-:|:-:|:-:|
|Member1|||||
|Member2|||||
|Member3|||||

```
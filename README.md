# Days_of_the_week
Calculate the day of the week for a given date.

usage: Week Day Calculator [-h] [-d DD] [-m MM] [-y YYYY]

Calculate the day of the week for given a date.
Output is formated as (day of the week) (day) (month) (year).

optional arguments:
  -h, --help  show this help message and exit
  -d DD       Day: 1 to 31
  -m MM       Month: 1 to 12
  -y YYYY     Year: integer limits

Exemple:
>> python3 week_day.py -d 23 -m 12 -y 2249
Samedi 23 Décembre 2249

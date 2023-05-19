import argparse;

week_days = {
	1: "Lundi",
	2: "Mardi",
	3: "Mercredi",
	4: "Jeudi",
	5: "Vendredi",
	6: "Samedi",
	7: "Dimanche"
}

months = {
	1: "Janvier",
	2: "Février",
	3: "Mars",
	4: "Avril",
	5: "Mai",
	6: "Juin",
	7: "Juillet",
	8: "Août",
	9: "Septembre",
	10: "Octobre",
	11: "Novembre",
	12: "Décembre"
}



def is_leap(year):
		if (year % 4 == 0):
			if (year % 100 == 0):
				if (year % 400 == 0):
					return True;
				else:
					return False;
			else:
				return True;
		else:
			return False;

def find_mod_year(year):

	mod = 0;
	
	if (year < 0):
		year += 1;
	while (year >= 2400):
		year -= 400;
	while (year < 2000):
		year += 400;
	while (year >= 2100):
		year -= 100;
		mod += 5;
	while (year >= 2004):
		year -= 4;
		mod += 5;
	if (year > 2000):
		mod += (year - 2000);
	return (mod % 7);

def find_mod_month(month, is_leap):
	
	mod = 0;
	
	while (month > 1):
		if (month == 2):
			if is_leap:
				mod += 29;
			else:
				mod += 28;
		elif (month in [4, 6, 9, 11]):
			mod += 30;
		else:
			mod += 31;
		month -= 1;
		
	return (mod % 7);

def day_exist(day, month, year):
	if (year == 0):
		return False;
	elif (day == 31):
		if (month in [2, 4, 6, 9, 11]):
			return False;
	elif (month == 2):
		if (day == 30 or (day == 29 and (not is_leap(year)))):
			return False;
	return True;

parser = argparse.ArgumentParser(
			prog='Week Day Calculator',
			formatter_class=argparse.RawTextHelpFormatter,
			description='Calculate the day of the week for given a date.\nOutput is formated as (day of the week) (day) (month) (year).',
			epilog='Exemple:\n>> python3 week_day.py -d 23 -m 12 -y 2249\nSamedi 23 Décembre 2249');

parser.add_argument('-d', metavar='DD', type=int, default=4,
			choices=range(1,32), help='Day: 1 to 31');

parser.add_argument('-m', metavar='MM', type=int, default=11,
			choices=range(1,13), help='Month: 1 to 12');

parser.add_argument('-y', metavar='YYYY', type=int, default=1999,
			help='Year: integer limits');

args = parser.parse_args();

if (not day_exist(args.d, args.m, args.y)):
	print('Day does not exist !');
	quit();

ymod = find_mod_year(args.y);
mmod = find_mod_month(args.m, is_leap(args.y));
tmod = ymod + mmod + args.d + 4;
wday = (tmod % 7) + 1;
print(week_days[wday], args.d, months[args.m], args.y);

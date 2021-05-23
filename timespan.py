from datetime import datetime, timedelta
def timespan(filename):
	intervals={}
	total=timedelta()
	with open(filename) as f:
		for line in f:
			interval,start_dt,start_time,dash, end_dt, end_time= line.strip().split()
			print(interval,start_dt,start_time,end_dt,end_time)
			start = datetime.strptime(start_dt+ ' ' +start_time, '%H:%M:%S %m/%d/%Y')
			end   = datetime.strptime(end_dt + ' ' +end_time, '%H:%M:%S %m/%d/%Y')

			intervals[interval]= end-start
			total += end-start
		print(f'{str(total/len(intervals))[:-7]}')
timespan('time.txt')

# import numpy as np
import pandas as pd
# import os
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


# Headers
# Account
# Date - DD/MM/YYYY
# Original Date - DD/MM/YYYY
# Description
# Original Description
# Amount
# Currency
# Category
# Budget

# Structure
# Headers
# Blank Row
# Data


# Categories =
# Bills
# Food & drink
# Experiences
# General
# Gift
# Giving
# Groceries
# Holidays
# Household
# Income
# Personal care
# Pub
# Savings
# Shopping
# Transfers
# Transport
# Unusual
# Work Lunches
# Work travel


def importTransactions(importFilename):
	'''Imports csv file'''
	df = pd.read_csv(importFilename, parse_dates=['Original Date'], infer_datetime_format=True, \
						index_col='Original Date', dtype={'Amount':'float64'})
	df2= df.loc[:, ["Amount", "Category", "Budget"]]
	df2.sort_index(ascending=True)
	return df2

def timeSpan(dfTimeSpan):
	dfTimeSpan.sort_index(ascending=True)
	dateEndYear, dateEndMonth = (dfTimeSpan.index[0].year, dfTimeSpan.index[0].month)
	# print (dateEnd)
	dateStartYear, dateStartMonth = (dfTimeSpan.index[-1].year, dfTimeSpan.index[-1].month)
	# print (dateStart)
	return dateEndYear, dateEndMonth, dateStartYear, dateStartMonth

def numberOfMonths(lastYear, lastMonth, firstYear, firstMonth):
	if (firstYear == lastYear):
		return lastMonth - firstMonth + 1
	elif (lastYear > firstYear):
		return (12 - firstMonth + lastMonth + 12*(lastYear-firstYear-1) + 1)
	else:
		return -1

def monthList(listStartYear, listStartMonth, listNumberOfMonths):
	out = []
	for i in range(listNumberOfMonths):
		j = int( (listStartMonth + i - 1) / 12)
		out.append(str(listStartYear + j ) + '-' + str(listStartMonth + i - 12 * j))
	return out

def overall (dfOverall):
	out, save = 0, 0 
	for value in dfOverall["Amount"]:
		if (value < 0):
			out += value
		elif (value > 0):
			save += value

	print(f'Out: \t£ {abs(round(out, 2))}')
	print(f'In: \t£ {abs(round(save, 2))}')
	if ((save + out) < 0):
		print(f'Net: \t£ ({abs(round((save + out), 2))})')
		return 0
	else:
		print(f'Net: \t£ {abs(round((save + out), 2))}')
		return 1

def monthly (dfMonthly):
	dateEndYear, dateEndMonth, dateStartYear, dateStartMonth = timeSpan(dfMonthly)

	Month = pd.DataFrame(index=(pd.date_range(start=(str(dateStartYear)+"-"+str(dateStartMonth)), \
					periods=numberOfMonths(dateEndYear, dateEndMonth, dateStartYear, dateStartMonth), \
					freq='M')), \
					dtype='float64')
	# print(numberOfMonths(dateEndYear, dateEndMonth, dateStartYear, dateStartMonth))

	dfBills 		= dfMonthly[dfMonthly["Category"] == "Bills"]
	dfFood_drink 	= dfMonthly[dfMonthly["Category"] == "Food & drink"]
	dfExperiences 	= dfMonthly[dfMonthly["Category"] == "Experiences"]
	dfGeneral 		= dfMonthly[dfMonthly["Category"] == "General"]
	dfGift 			= dfMonthly[dfMonthly["Category"] == "Gift"]
	dfGiving 		= dfMonthly[dfMonthly["Category"] == "Giving"]
	dfGroceries 	= dfMonthly[dfMonthly["Category"] == "Groceries"]
	dfHolidays 		= dfMonthly[dfMonthly["Category"] == "Holidays"]
	dfHousehold 	= dfMonthly[dfMonthly["Category"] == "Household"]
	dfIncome 		= dfMonthly[dfMonthly["Category"] == "Income"]
	dfPersonalcare 	= dfMonthly[dfMonthly["Category"] == "Personal care"]
	dfPub 			= dfMonthly[dfMonthly["Category"] == "Pub"]
	dfSavings 		= dfMonthly[dfMonthly["Category"] == "Savings"]
	dfShopping 		= dfMonthly[dfMonthly["Category"] == "Shopping"]
	dfTransfers 	= dfMonthly[dfMonthly["Category"] == "Transfers"]
	dfTransport 	= dfMonthly[dfMonthly["Category"] == "Transport"]
	dfUnusual 		= dfMonthly[dfMonthly["Category"] == "Unusual"]
	dfWorkLunches 	= dfMonthly[dfMonthly["Category"] == "Work Lunches"]
	dfWorktravel 	= dfMonthly[dfMonthly["Category"] == "Work travel"]

	months = monthList(dateStartYear, dateStartMonth, \
		numberOfMonths(dateEndYear, dateEndMonth, dateStartYear, dateStartMonth))

	for month in months:
		Month.at[month, 'Bills'] 			= dfBills.loc[month, 'Amount'].sum()
		Month.at[month, "Food & drink"] 	= dfFood_drink.loc[month, 'Amount'].sum()
		Month.at[month, "Experiences"] 		= dfExperiences.loc[month, 'Amount'].sum()
		Month.at[month, "General"] 			= dfGeneral.loc[month, 'Amount'].sum()
		Month.at[month, "Gift"] 			= dfGift.loc[month, 'Amount'].sum()
		Month.at[month, "Giving"] 			= dfGiving.loc[month, 'Amount'].sum()
		Month.at[month, "Groceries"] 		= dfGroceries.loc[month, 'Amount'].sum()
		Month.at[month, 'Holidays'] 		= dfHolidays.loc[month, 'Amount'].sum()
		Month.at[month, 'Household'] 		= dfHousehold.loc[month, 'Amount'].sum()
		Month.at[month, 'Income'] 			= dfIncome.loc[month, 'Amount'].sum()
		Month.at[month, 'Personal care'] 	= dfPersonalcare.loc[month, 'Amount'].sum()
		Month.at[month, 'Pub'] 				= dfPub.loc[month, 'Amount'].sum()
		Month.at[month, 'Savings'] 			= dfSavings.loc[month, 'Amount'].sum()
		Month.at[month, 'Shopping'] 		= dfShopping.loc[month, 'Amount'].sum()
		Month.at[month, 'Transfers'] 		= dfTransfers.loc[month, 'Amount'].sum()
		Month.at[month, 'Transport'] 		= dfTransport.loc[month, 'Amount'].sum()
		Month.at[month, 'Unusual'] 			= dfUnusual.loc[month, 'Amount'].sum()
		Month.at[month, 'Work Lunches'] 	= dfWorkLunches.loc[month, 'Amount'].sum()
		Month.at[month, 'Work travel'] 		= dfWorktravel.loc[month, 'Amount'].sum()
	
	# summaryStats
	print (Month)
	# print (Month.describe())
	print (f'{Month.mean()}')


def budgetSweep (filename):
	# out = 0
	# save = 0

	dfTransactions = importTransactions (filename)

	plt.close("all")

	overall (dfTransactions)

	monthly (dfTransactions)


	###################### Play Zone
	# trendMonth = Month.cumsum()
	# trendMonth.plot()
	# plt.show()

	###################### Play Zone End

	trendOA = dfTransactions["Amount"].cumsum()
	# print (trend)
	trendOA.plot()
	# plt.show()

	# print (dfTransactions)
	return None

# budgetSweep ('transactions.csv')

budgetSweep ('transactions2.csv')
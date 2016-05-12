
# coding: utf-8

import requests
import pandas
import argparse
from datetime import *; from dateutil.relativedelta import *


parser = argparse.ArgumentParser(description = 'APIKey and EnrollId Parser')
parser.add_argument('-e' , nargs='?', action='store', default='100', dest='enrollId')
parser.add_argument('-k', nargs='?', action='store', default='eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlE5WVpaUnA1UVRpMGVPMmNoV19aYmh1QlBpWSJ9.eyJFbnJvbGxtZW50TnVtYmVyIjoiMTAwIiwiSWQiOiIxZGFiNDdkZS1lZGYxLTQ4YmItODA0My1lNTE5NTZhYTFlZGYiLCJSZXBvcnRWaWV3IjoiRW50ZXJwcmlzZSIsIlBhcnRuZXJJZCI6IiIsIkRlcGFydG1lbnRJZCI6IiIsIkFjY291bnRJZCI6IiIsImlzcyI6ImVhLm1pY3Jvc29mdGF6dXJlLmNvbSIsImF1ZCI6ImNsaWVudC5lYS5taWNyb3NvZnRhenVyZS5jb20iLCJleHAiOjE0NzU4NzU5MjUsIm5iZiI6MTQ2MDA2NDcyNX0.f2BVlai4zsfZ263PrieDNiou5jHF9V3NztOvmyYKWAQqoKZJQRD_i7ISXWz--uDOOG9DfN60j8C2svCDzBvtMzHN5c5Tz-woVJz-hDnBNV1EHF172QcpRoDoZ3L8v2vgOoiYdrGtsWWKHKmz-3iQczTYH-FM3EiIPh5RJeRxbeQPjPjNhdbmgUcPfrK-tIPTvbksY8OWvvJPPY02dTWkaMR7vhsExF1Pd7Jv8eaBPl6jDpTxL_kCAwYCqOqyWoAwRaHqAz-5nybS_hCkfwESYd9dXTjn3uzLz0YDKCzhf9wFgwg1XHeDrIPT85UCZEti9Ct5gBH2j5-lOyrmm3nVwA', dest='apiKey')
args = parser.parse_args({})

baseUrl = 'https://ea.azure.com'
prevMonths = [(str(d.year) + '-' + str(d.month)) for d in [date.today()+relativedelta(months=-m) for m in range(1,13)]]
allTables = pandas.DataFrame([])

for month in prevMonths:
    myHeads = {'authorization' : 'bearer ' + args.apiKey}
    myParams = {'month' : month, 'Type' : 'Detail', 'fmt' : 'json'}
    reportUri = baseUrl + '/rest/' + args.enrollId + '/usage-report'
    myReport = requests.get(reportUri, params = myParams, headers = myHeads)
    myTable = pandas.read_json(myReport.text)
    allTables = allTables.append(myTable)

allTables.to_csv('prev12.csv', index=False)

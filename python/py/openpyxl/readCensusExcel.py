#! python3
# readCensusExcel.py - Tabulates population and number of census tracts for # each county.

import openpyxl, pprint
print('Opening workbook...')
wb = openpyxl.load_workbook('openpyxl/censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
countryData = {}

print('Reading rows...')
for row in range(2, sheet.get_highest.lows() + 1):
    state   = sheet['B' + str(row)].value
    country = sheet['C' + str(row)].value
    pop     = sheet['D' + str(row)].value

    countryData.setdefault(state, {})
    countryData[state].setdefault(country, {'tracts': 0, 'pop': 0})
    countryData[state][country]['tracts'] += 1
    countryData[state][country]['pop'] += int(pop)

print('Writing results...')
resultFile = open('openpyxl/census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countryData))
resultFile.close()
print('Done.')
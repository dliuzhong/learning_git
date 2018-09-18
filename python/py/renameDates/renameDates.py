#!python3 
# renameDates.py - Rename filenames with American MM-DD-YYY date format
# to European DD-MM-YYYY

import shutil, os, re
# Create a regex that matches files with the American date format.
datePattern = re.compile(r"""^(.*?)  # all text before the date, see 7.10
    ((0|1)?\d)-                     # one or two digits for the month
    ((0|1|2|3)?\d)-                 # one or two digits for the day
    ((19|20)\d\d)                   # four digits for the year
    (.*?)$                          # all text after the date
""", re.VERBOSE)

#TO-DO: Loop over the files in the working directory.
for amerFilename in os.listdir('./renameDates'):
    mo = datePattern.search(amerFilename)
    #TO-DO: Skip files without a date.
    if mo == None:
        continue
    #TO-DO: Get the different parts of the filenames.
    #print()
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    #TO-DO: Form the European-style filename.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    #TO-DO: Get the full, absolute file paths.
    absWorkDir = os.path.abspath('./renameDates')
    amerFilename = os.path.join(absWorkDir, amerFilename)
    euroFilename = os.path.join(absWorkDir, euroFilename)

    #TO-DO: Rename the files
    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    shutil.move(amerFilename, euroFilename)

#!/usr/bin/env python
from cakecmsutils import ExtendedCakeCMS

HOST = 'https://cms.cispa.saarland'
TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxx'
COURSE = 'ver2122'

cms = ExtendedCakeCMS(HOST, token=TOKEN, course=COURSE)

# Download files in category 'Lecture Slides' to directory slides and
# filter out slides that have 'preliminary' in their filename.
cms.download_category('Lecture Slides', 'slides', lambda s : 'preliminary' in s, pad_digits=2)
print()
cms.download_category('Problem Sets', 'problems')
print()
cms.download_category('Project', 'project_docs')

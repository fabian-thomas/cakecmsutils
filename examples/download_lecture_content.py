#!/usr/bin/env python
from cakecmsutils import ExtendedCakeCMS

HOST = 'https://cms.cispa.saarland'
TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxx' # TODO: replace with your token

cms = ExtendedCakeCMS(HOST, token=TOKEN, course='ver2122')

# Download files in category 'Lecture Slides' to directory slides and
# filter out slides that have 'preliminary' in their filename.
cms.download_category('Lecture Slides', 'slides', lambda s : 'preliminary' in s)
print()
cms.download_category('Problem Sets', 'problems')
print()
cms.download_category('Project', 'project_docs')

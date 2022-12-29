from cakecms import CakeCMS
import json
import os
import pickle

CACHE_FILE = '.cakecmscache'

def user_confirm(question):
    selection = input(question + ' [y/N] ')
    if selection == 'y' or selection == 'Y':
        return True
    else:
        return False

class ExtendedCakeCMS(CakeCMS):
    def __init__(self, url, token=None, course='system'):
        if os.path.exists(CACHE_FILE):
            with open(CACHE_FILE, 'rb') as fd:
                self.cache = pickle.load(fd)
        else:
            self.cache = {}
            self.cache['files'] = {}
        super().__init__(url, token, course)

    def download_category(self, category_name, output_dir, filter_fun=None):
        print('Downloading category:', category_name)
        categories = list(filter(lambda c: c['MaterialCategory']['name'] == category_name, self.materials_index()))

        if len(categories) == 0:
            category = categories[0]
        else:
            raise Exception("Category not found. Possible categories:", [c['MaterialCategory']['name'] for c in self.materials_index()])

        os.makedirs(output_dir, exist_ok=True)
        remote_files = set()

        found_new = False
        for file in category['MaterialFile']:
            new_revision = False

            if filter_fun != None and filter_fun(file['name']):
                # file rejected by filter
                continue
            if file['id'] in self.cache['files']:
                metadata_entry = self.cache['files'][file['id']]
                if os.path.exists(os.path.join(output_dir, metadata_entry['filename'])):
                    if metadata_entry['revision'] >= file['revision']:
                        # we have the lastest revision, so skip download
                        remote_files.add(metadata_entry['filename'])
                        continue
                    else:
                        new_revision = True

            # download file
            response = self.material_download(file['id'])
            filename = response[0]
            filepath = os.path.join(output_dir, filename)
            with open(filepath, 'wb') as fd:
                fd.write(response[1])
            remote_files.add(filename)

            # save metadata to cache
            metadata_entry = {}
            metadata_entry['filename'] = filename
            metadata_entry['revision'] = file['revision']
            self.cache['files'][file['id']] = metadata_entry

            # print
            if new_revision:
                print('New revision ({}):'.format(file['revision']), filename)
            else:
                print('New file:', filename)

            found_new = True

        if not found_new:
            print('No new files')

        # check for files that are not on remote anymore
        diff = set(os.listdir(output_dir)).difference(remote_files)
        if len(diff) > 0:
            print()
            for filename in diff:
                if user_confirm('File {} is not on remote. Delete?'.format(filename)):
                    os.remove(os.path.join(output_dir, filename))

        self.write_cache()

    def write_cache(self):
        with open(CACHE_FILE, 'wb') as fd:
            pickle.dump(self.cache, fd)

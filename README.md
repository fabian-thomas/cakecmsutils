# cakecmsutils

Python scripts to interact with the [CakeCMS API](https://cms.cispa.saarland/system/help/api).

## Installation of the python module

```bash
make install
```

You may need to adjust the Makefile to match your python version.
For windows systems one may need to adjust the makefile as well. Please post a PR if someone knows how to set this up correctly.

## Example scripts:

For obtaining the right values for `HOST`, `TOKEN` and `COURSE` refer to [CakeCMS API](https://cms.cispa.saarland/system/help/api).

### Download course materials (examples/download_course_content.py)

This script may be used to download course materials by category. The example script also shows how a negative filter may be used to skip some of the files. Note that `ExtendedCakeCMS` writes data to a hidden cache file in your PWD. This cache file makes sure that no files need to be redownloaded.

This script should probably be copied to a seperate directory for each of your courses and then adjusted to match the categories. The category titles are the ones visible in the headers on the webpage.
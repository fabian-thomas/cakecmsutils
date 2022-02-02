Python scripts to interact with the [CakeCMS API](https://cms.cispa.saarland/system/help/api).

## Installation of the python module

### Prerequisites (in both below cases)

The [cakecms module](https://gitea.mk-bauer.de/CakeCMS/CakeCMS-Python-API) has to be installed first.

### From PyPi

```bash
pip install cakecmsutils
```

### From source

Install the PyPI package `build`:
```bash
pip install build
```

Then (from the root of the repo):
```bash
python -m build
pip install dist/*.whl
```

## Example scripts

For obtaining the right values for `HOST`, `TOKEN` and `COURSE` refer to [CakeCMS API](https://cms.cispa.saarland/system/help/api).

### Download course materials (examples/download_course_materials.py)

This script may be used to download course materials by category. The example script also shows how a negative filter may be used to skip some of the files. Note that `ExtendedCakeCMS` writes data to a hidden cache file in your PWD. This cache file makes sure that no files need to be redownloaded.

This script should probably be copied to a separate directory for each of your courses and then adjusted to match the categories. The category titles are the ones visible in the headers on the webpage.

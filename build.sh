# deacivate the current env
deactivate

# remove the dist directory (may not be empty)
rm -rf dist

# build the package
python3 -m build

# publish the package with twine
# python3 -m twine upload --repository testpypi dist/*

# remove the current virtual env for testing
rm -rf .venv

# create a new virtual environment for testing
python3 -m venv .venv

# activate the new environment
source .venv/bin/activate

# install the dist
pip install dist/ignorepy_sprousecal-0.0.7-py3-none-any.whl

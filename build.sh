# build the distribution packages
python -m build

# install the local dist packages
pip install dist/ignorepy-0.1.0-py3-none-any.whl --force-reinstall

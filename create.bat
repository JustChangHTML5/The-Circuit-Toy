rm -rf dist build
#pyinstaller --onefile main.py
pyinstaller --onefile -w main.py
copy *.txt dist
copy *.jpg dist
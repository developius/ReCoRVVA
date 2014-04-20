import os

print("Downloading module 'termcolor'")
os.system("wget https://pypi.python.org/packages/source/t/termcolor/termcolor-1.1.0.tar.gz")
print("Extracting termcolor...")
os.system("tar zxvf termcolor-1.1.0.tar.gz")
print("Building and installing termcolor...")
os.system("cd termcolor-1.1.0; python setup.py build; sudo python setup.py install")
print("Successfully installed termcolor! - cleaning up")
os.system("rm -r termcolor*")
print("Done")


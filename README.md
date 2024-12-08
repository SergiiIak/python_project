# Python Project

(Solution for the job interview, Institut für Informatik, Universität Göttingen)


### Project description

A new Python project that meets the following requirements:
The project should be scalable, maintainable, readable, and reusable so that your team members can build upon it.

### Initial Functionality

A Function [count_vowels](./eng_vowels/vowels.py) that counts the vowels of the English alphabet in a given string of arbitrary length is implemented.


### Application launch

Please open terminal in the project's folder and enter the command:
```
python main.py
```

### Requirements

Make sure Python is installed on your system and available in the terminal.
The given application was tested successfully on Python 3.10.9 and Python 3.12.8.

In order to generate test coverage reports, install requirements.txt using following command:
```
pip install -r requirements.txt
```

### Tests

Project contains [unit tests](./tests/test_count_vowels.py) and [test coverage report](./htmlcov/index.html).
You can open the test coverage report in your browser using following commands in the terminal:

Linux:
```
open htmlcov/index.html
```
Windows:
```
start htmlcov\index.html
```

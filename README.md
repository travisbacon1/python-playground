# Getting started

## Get Python
1) Download Python3 for Mac (https://www.python.org/downloads/release/python-392/)
2) Open up a Terminal (either in VSCode or using `CMD + Space` and searching for "Terminal")
3) Run `Python3 --version` to make sure it's 3.x.x

## Running Python files

1) In your terminal window, navigate to the directory containing a Python file using `cd` (see https://maker.pro/linux/tutorial/basic-linux-commands-for-beginners for details)
2) Type `Python3 <your_file_name.py>`

## Running Python files in the terminal or Jupyter Notebook

Jupyter Notebooks are a great way of running Python scripts (especially in data science), but can get messy. When you run a Python file with `Python3 <your_file_name.py>` this is what happens:

1) A Python interpreter is opened
2) The interpreter then reads your script in and executes it all in one fell swoop (though not necessarily top-to-bottom, see the `python_file_anatomy.md` file for more details)
3) The Python interpreter closes successfully (or crashes out if you have errors)
   
This means all the variables you declare and use in the script are declared, assigned, used and then **forgotten**.

Jupyter Notebooks are slightly different, in this case a Python interpreter is opened and **remains open** as a session(that's why you see that little Terminal window pop up on MacBooks). You can then run your script all at once (similar to using `Python3 <your_file_name.py>`) or run select cells (containing isolated bits of code) in any order. Running these cells out of order could have odd consequences and lead to lots of error messages (most likely related to undeclared errors or undeclared functions).
# cs325-hw1-closest-pair

finding the closest pair in many ways


# Creating test files

right now we have a create_files.py but basically thats just a "bash" script of for loops that uses the helperlibrary functoin createTestFile()

which takes the arguments (file_path,number_size,number_of_items), so you can use that to create your own.

# execution

if you want to run the execution with on of our sample files, run ``` python create_files.py  ``` and then you will have the files.

after that there are three different searching functions, and they are all contained within ** tester.py ** .

the generic way of invoking the program:

``` python tester.py <method> <file> ```
where <method>:
  brute || naive || advanced

and file is:
 "1" - "8" if you want to use our sample files or
 "relative-path.txt" if you want to use your own sample file.

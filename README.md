# cs325-hw1-closest-pair

finding the closest pair in many ways


# Creating test files

right now we have a create_files.py but basically thats just a "bash" script of for loops that uses the helperlibrary functoin createTestFile()

which takes the arguments (file_path,number_size,number_of_items), so you can use that to create your own.

# execution

if you want to run the execution with our sample files and testing procedures, run ``` python create_files.py  ``` and then you will have the files.

after that there are three different searching functions, and they are all contained within **tester.py** .

the generic way of invoking the program:

``` python tester.py <method> <file> ```
where "method" can be one of three: <br />
  brute || naive || advanced <br />

and "file" is: <br />
 "1" - "8" if you want to use our sample files or <br />
 "relative-path.txt" if you want to use your own sample file.

example:

```python tester.py naive smallfile.txt``` 
<br />
runs the naive algorythm once with the file smallfile.txt in the current working directory.
<br />
or
<br />
```python tester.py naive 2``` 
<br />
this runs the naive algorythm 10 times with all the sample files contained in ```./files/size2/```


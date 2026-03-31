## Python for Everybody

This course has been created by Professor Charles Severance from the University of Michigan.
> Learn to Program and Analyze Data with Python. Develop programs to gather, clean, analyze, and visualize data.

**Link**: <https://www.py4e.com/lessons>

**Textbook**: [PDF](http://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf) / [EPUB](http://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.epub) / [HTML](https://www.py4e.com/html3) / [Buy hardcopy](https://www.py4e.com/book)

**Note**: This course is also offered on Coursera, Edx. Those versions require you to pay to get the full version of the course. We suggest doing the course on its website, which is completely free.

### Instructions

- You need to [sign in](https://www.py4e.com/) to the course website using your Google account to access the assignments.
- Watch all the videos of a lesson and then do its assignments.
- If you prefer reading books, you can read the HTML version of the chapter related to the lesson linked on the lesson's page, or you can download the whole book in different formats from [this page](https://www.py4e.com/book).
- If you face any problems, feel free to ask questions. You can join the OSSU chat for this course here: <https://discord.gg/syA242Z>.
- You only need to complete the course up to the Regular Expressions lesson. The rest of the course is optional.

### Course Materials

1. [Installing Python](https://www.py4e.com/lessons/install)
2. [Why Program?](https://www.py4e.com/lessons/intro)
3. [Variables, expressions and statements](https://www.py4e.com/lessons/memory)
4. [Conditional Execution](https://www.py4e.com/lessons/logic)
5. [Functions](https://www.py4e.com/lessons/functions)
6. [Loops and Iterations](https://www.py4e.com/lessons/loops)
7. [Strings](https://www.py4e.com/lessons/strings)
8. [Files](https://www.py4e.com/lessons/files)
9. [Lists](https://www.py4e.com/lessons/lists)
10. [Dictionaries](https://www.py4e.com/lessons/dictionary)
11. [Tuples](https://www.py4e.com/lessons/tuples)
12. [Regular Expressions](https://www.py4e.com/lessons/regex)
13. [Network Programming](https://www.py4e.com/lessons/network) (Optional)
14. [Using Web Services](https://www.py4e.com/lessons/servces) (Optional)
15. [Object-Oriented Programming](https://www.py4e.com/lessons/Objects) (Optional)
16. [Databases](https://www.py4e.com/lessons/database) (Optional)
17. [Data Visualization](https://www.py4e.com/lessons/dataviz) (Optional)

### Fixes

1. If you're doing the BeautifulSoup4 lesson, there is an issue with Python 3.10+ that will give you an error referencing the Collections library. We have a fix for you. We don't expect you to understand it, just put this in front of your code in the imports block:

```python
import collections
collections.Callable = collections.abc.Callable

from bs4 import BeautifulSoup 
```

Doing this should fix the compatibility issue and allow your code to run.

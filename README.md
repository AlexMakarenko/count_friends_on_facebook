# This is an example how to count friends on facebook using Selenium WebDriver and Python. 
For less code I used wrapper for Selenium: [Elementium](https://github.com/actmd/elementium).


To run the code you need to install all dependencies from requirement.txt:
```
pip install -r requirements.txt
```

In the `tests.test_count_fiends_on_facebook.py` edit constants and enter real `FB_EMAIL` and `FB_PASS`.

Then you can run the test using pytest:
```
pytest tests
```
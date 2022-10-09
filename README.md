# flask_input_app
Flask App which runs Python user-defined function for html-form input field and return result back to html text area as an output.

For me it's an extremely common case to test and embed Python functionality into
web app. That's why this repo exists.

# How it works

1. Flask serves webpage welcome.html
2. User writes text into text input.
3. User clicks "Generate" button
4. Python user-defined function `special_f` executes on the input.
5. User gets the result of `special_f` in textarea in Output section.

# Preview

<img src="doc/html_browser.png" alt="alt text" width="600"/>

# Run
Linux:
```
export FLASK_APP=app.py
flask run
```
Windows:
```
set FLASK_APP=app.py
flask run
```

Check http://localhost:5000/action url.

# Cheatsheet

One-page cheatsheet [doc](doc/cheatsheet.pdf).

# Simple web app with Flask

## Getting started

### Open a terminal inside the `./mini_app` folder

### You can run the server in debug mode with

``` bash
flask --app hello run --debug
 * Serving Flask app 'hello'
 * Debug mode: on
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: nnn-nnn-nnn
```

> With the debug mode, the server will automatically reload your changes in the code.

If you trust the users in your network, you can tell your operating system to listen on all public IP by using:

``` bash
$ flask run --host=0.0.0.0
```

## Access the web app in your preferred browser

Type this URL:

> <http://127.0.0.1:5000>

Or introduce your name to be greeted by the app:

> Or <http://127.0.0.1:5000\\\<name>

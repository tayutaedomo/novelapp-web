# novelapp-web

## Setup
```
$ git clone git@github.com:tayutaedomo/novelapp-web.git
$ cd novelapp-web
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```


## git lfs
You have to execute the following commands as use git lfs.
```
$ git lfs install
```


## Local Server
```
$ cd flask-sandbox
$ python app.py
$ open "http://127.0.0.1:5000/"
```
Basic Auth: novelapp / novels


## Config ENV
You should set the appropriate ENV.
```
$ export APP_SETTINGS="config.DevelopmentConfig"
# or
$ export APP_SETTINGS=config.StagingConfig
# or
$ export APP_SETTINGS=config.ProductionConfig
```


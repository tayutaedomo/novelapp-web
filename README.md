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
$ cd novelapp-web
$ python app.py
$ open "http://127.0.0.1:5000/"
```
Basic Auth: novelapp / novels


## Docker
```
$ cd novelapp-web
$ docker build -t novelapp-web .
$ docker run --rm -it -e PORT=8080 -p 8080:8080 novelapp-web
$ open 'http://0.0.0.0:8080'
```


## Config ENV
You should set the appropriate ENV.
```
$ export APP_SETTINGS="config.DevelopmentConfig"
# or
$ export APP_SETTINGS=config.StagingConfig
# or
$ export APP_SETTINGS=config.ProductionConfig
```


## Cloud Run
```
$ cd novelapp-web
$ gcloud builds submit --tag gcr.io/[PROJECT-ID]/novelapp-web
$ gcloud run deploy --image gcr.io/[PROJECT-ID]/novelapp-web --platform managed
```

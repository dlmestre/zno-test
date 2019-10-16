Using `docker` to build the project:

```
docker build -t getdata .
docker run -e URL=https://api/v1/logs/ -e DATE=8-4-2018 -it getdata
```

To run the app locally (on the folder C1/app):

python3 app.py -d "8-4-2018" -u "https://api.localytics.com/v1/logs/"

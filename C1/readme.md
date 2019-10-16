Using `docker` to build the project:

```
docker build -t getdata .
docker run -e URL=https://api/v1/logs/ -e DATE=8-4-2018 -it getdata
```

To run the app locally (on the folder C1/app):

python3 app.py -d "8-4-2018" -u "https://api/v1/logs/"

app.py creates a tree folder structure : 2018/4/8/export.csv

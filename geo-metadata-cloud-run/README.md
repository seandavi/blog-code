## Usage

```
git clone ....
cd blog-code/geo-metadata-cloud-run
docker build -t seandavi/geometadata-cloud-run .
# test
docker run -p 8000:80 seandavi/geometadata-cloud-run
# in another terminal
curl http://localhost:8000/GSE2553
# returns json
gcloud run deploy gcloud run deploy --image gcr.io/PROJECT-ID/helloworld --platform managed
# returned value is the URL of your app
```

When completed:

```
gcloud run delete 
```

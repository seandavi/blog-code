Code for https://seandavi.github.io/post/cloud-run-notes/


# Usage

## locally deploy docker-based api

```
git clone ....
cd blog-code/geo-metadata-cloud-run
# choose your own 
docker build -t seandavi/geometadata-cloud-run .
# test
docker run -p 8000:80 seandavi/geometadata-cloud-run
# in another terminal
curl http://localhost:8000/GSE2553
# returns json
```

## Build and deploy to google cloud platform

You will probably need to enable the cloud run API on google. See the cloud run tutorial from google.

```
export PROJECT_ID=<YOUR-GOOGLE-PROJECT>
docker build -t gcr.io/${PROJECT_ID}/geometadata-cloud-run
gcloud run deploy gcloud run deploy --image gcr.io/${PROJECT_ID}/geometadata-cloud-run --platform managed
```

You will get a URL that your application will respond to. Then, you can paste this URL into your browser or run using curl:

- https://YOUR_URL_FROM_ABOVE/GSE2553

## Delete the google cloud work

When completed:

```
gcloud run delete ...
```

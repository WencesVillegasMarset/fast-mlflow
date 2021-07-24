# Fast MLflow setup

## Configuration

To setup an S3 Bucket for storing MLFlow's artifacts (only way to write artifacts with this setup), change MLFLOW_ARTIFACT_ROOT variable in .env file

```
MLFLOW_ARTIFACT_ROOT=s3://<bucket>/<path>
```

Then `docker-compose up` will get you up and running.

For default settings check `.env`.

AWS credentials can be passed by mounting `~/.aws`.

### Updating to newer MLflow versions

Uncomment the line `mlflow db upgrade` in [mlflow/start.sh](./mlflow/start.sh) in order to run the db migrations.

Note: This is only necessary when updating not on the first setup.

### Setting up authentication.

Usually you would set up an NGINX proxy with authentication, here are some resources:

* https://towardsdatascience.com/managing-your-machine-learning-experiments-with-mlflow-1cd6ee21996e
* https://stackoverflow.com/questions/58956459/how-to-run-authentication-on-a-mlflow-server
* https://docs.nginx.com/nginx/admin-guide/security-controls/configuring-http-basic-authentication/

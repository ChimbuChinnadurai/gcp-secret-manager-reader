import os
from google.cloud import secretmanager

PROJECT_ID = os.environ['PROJECT_ID']
SECRET_NAME = os.environ['GCP_SECRET_NAME']
SECRET_MOUNT_LOCATION = os.environ['SECRET_MOUNT_LOCATION']


def _get_secret(project_id, secret_name, version_id="latest") -> str:
    client = secretmanager.SecretManagerServiceClient()
    name = f'projects/{project_id}/secrets/{secret_name}/versions/{version_id}'
    response = client.access_secret_version(request={"name": name})
    gcp_secret = response.payload.data.decode("UTF-8")
    return gcp_secret


if __name__ == "__main__":
    secret = _get_secret(PROJECT_ID, SECRET_NAME)
    with open(SECRET_MOUNT_LOCATION, "w") as file:
        file.write(secret)

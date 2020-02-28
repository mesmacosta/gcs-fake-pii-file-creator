# gcs_fake_pii_file_creator

Library for creating CSV files in GCS with fake pii data.

The drive and use case to create this library, was when you need a lot of data to validate if your org complies with regulations like
CCPA, HIPAA, GDPR.


## 1. Environment setup

### 1.1. Get the code

````bash
git clone https://.../gcs_fake_pii_file_creator.git
cd gcs_fake_pii_file_creator
````

### 1.2. Auth credentials

##### 1.2.1. Create a service account and grant it below roles

The Service Account authenticated must have administrator privileges for Cloud Storage and BigQuery.

##### 1.2.2. Download a JSON key and save it as
- `<YOUR-CREDENTIALS_FILES_FOLDER>/gcs_fake_pii_file_creator-credentials.json`

> Please notice this folder and file will be required in next steps.

### 1.3. Virtualenv

Using *virtualenv* is optional, but strongly recommended unless you use Docker or a PEX file.

##### 1.3.1. Install Python 3.6+

##### 1.3.2. Create and activate a *virtualenv*

```bash
pip install --upgrade virtualenv
python3 -m virtualenv --python python3 env
source ./env/bin/activate
```

##### 1.3.3. Install the dependencies

```bash
pip install --editable .
```

##### 1.3.4. Set environment variables

Replace below values according to your environment:

```bash
export GOOGLE_APPLICATION_CREDENTIALS=credentials_file_path

```

### 1.4. Docker

See instructions below.

## 2. Sample application entry point

### 2.1. Run main.py

- Virtualenv

Only the project-id argument is required.

```bash
python main.py --project-id your_project --num-rows 5000 --num-cols 10 --obfuscate-col-names true
```

### 2.2. Or using Docker

```bash
docker build -t gcs_fake_pii_file_creator .
docker run --rm --tty -v CREDENTIALS_FILES_FOLDER:/data \
gcs_fake_pii_file_creator \
 --project-id your_project
```

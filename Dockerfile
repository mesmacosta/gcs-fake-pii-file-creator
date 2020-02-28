# docker build -t gcs_fake_pii_file_creator .
FROM python:3.7

# Set the GOOGLE_APPLICATION_CREDENTIALS environment variable.
# At run time, /data must be binded to a volume containing a valid Service Account credentials file
# named gcs_fake_pii_file_creator-credentials.json.
ENV GOOGLE_APPLICATION_CREDENTIALS=/data/gcs_fake_pii_file_creator-credentials.json

WORKDIR /app

# Copy project files (see .dockerignore).
COPY . .

# Install gcs-file-creator package from source files.
RUN pip install .

ENTRYPOINT ["python", "main.py"]

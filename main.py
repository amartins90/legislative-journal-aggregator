from dotenv import load_dotenv
import os

from scraper import Scraper
from minio_client import MinioConnection

# TODO add ruff
# TODO add githubactions
# TODO add .gitignore
# TODO add cities IBGE code list

def main():
    load_dotenv()
    house_url = os.getenv("LEGISLATIVE_HOUSE_URL")
    bucket_name = os.getenv("BUCKET_NAME")

    # MinIO settings
    minio_url = os.getenv("MINIO_URL")
    minio_username = os.getenv("MINIO_USERNAME")
    minio_password = os.getenv("MINIO_PASSWORD")

    scraper = Scraper(house_url)
    print(scraper.get_latest_editions())

    minio_connection = MinioConnection(minio_url, minio_username, minio_password)
    minio_connection.validate_bucket(bucket_name)

if __name__ == "__main__":
    main()

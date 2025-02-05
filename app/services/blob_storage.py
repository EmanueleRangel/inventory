from azure.storage.blob import BlobServiceClient
import os
from dotenv import load_dotenv # type: ignore

load_dotenv()

AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")  
CONTAINER_NAME = os.getenv(CONTAINER_NAME)

blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)
container_client = blob_service_client.get_container_client(CONTAINER_NAME)

def upload_to_blob_storage(file, filename: str) -> str:
    """Faz o upload de um arquivo para o Azure Blob Storage e retorna a URL."""
    blob_client = container_client.get_blob_client(filename)
    blob_client.upload_blob(file, overwrite=True)
    return blob_client.url

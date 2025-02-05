from fastapi import APIRouter, File, UploadFile, HTTPException
from app.services.blob_storage import upload_to_blob_storage

router = APIRouter()

@router.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    try:
        blob_url = upload_to_blob_storage(file.file, file.filename)
        return {"message": "Upload realizado com sucesso!", "blob_url": blob_url}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao fazer upload: {e}")

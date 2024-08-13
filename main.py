import os
from typing import Annotated

from fastapi import FastAPI, File, UploadFile, HTTPException, status
from fastapi.responses import FileResponse

app = FastAPI()
DOWNLOAD_DIR = 'C://Users//Public//Documents//RingCentral Setup//rec'

'''
@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"file": file.filename}
'''

@app.get("/allfiles/")
async def list_file_list():
    list = os.listdir(DOWNLOAD_DIR)
    return list

@app.get("/download/{file}")
async def download_file(file: str):
    list = os.listdir(DOWNLOAD_DIR)

    if file not in list:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    return FileResponse(path=os.path.join(DOWNLOAD_DIR, file),
                        media_type="application/octet-stream",
                        filename=file)
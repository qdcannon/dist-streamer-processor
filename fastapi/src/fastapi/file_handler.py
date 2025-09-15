from fastapi import FastAPI, File, UploadFile
import httpx

app = FastAPI()
OCA_URL = "http://cxx-service:8081/process"  # k8s service or docker network alias

@app.post("/process") #process will handle all POST requests for process endpoint
async def process(file: UploadFile = File(...)):
    #read the uploaded image bytes
    img_bytes = await file.read()

    #forward to image to opencv app container
    async with httpx.AsyncClient() as client:
        r = await client.post(OCA_URL, content=img_bytes)
    return {"processed_image": r.content}  # or stream back as file response

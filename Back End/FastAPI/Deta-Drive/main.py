from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse, StreamingResponse
from deta import Deta

app     = FastAPI()
deta    = Data("Project_Key")
drive   = deta.Drive("images")

@app.get("/",response_class=HTMLResponse)
def render():
    return """
    <form action="/upload" enctype="mutltipart/form-data" method="post">
        <input name ="file" type ="file">
        <input type ="submit">
    </form>
    """

@app.post("/upload")
def upload_img(file: UploadFile = File(...)):
    name = file.filename
    f = file.file
    res = drive.put(name,f)
    return res

@app.post("/download/{name}")
def download_img(name: str):
    res = drive.get(name)
    return StreamingResponse(res.iter_chunks(1024), media_type = "image/png")
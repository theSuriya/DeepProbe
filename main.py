import uvicorn
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS (Cross-Origin Resource Sharing)
origins = [
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ...

# Serve static files from the "static" directory inside the "frontend" folder
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

# ...


# Templates directory for Jinja2
templates = Jinja2Templates(directory="templates")

# Trusted Host Middleware to prevent "Host header attack"
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/chatbot")
async def get_chatbot_response():
    # Here you can implement the logic to communicate with Dialogflow
    # and retrieve the chatbot response.
    # Replace the following return statement with your Dialogflow integration code.
    return {"response": "Chatbot response from FastAPI"}



if __name__ == '__main__':
    uvicorn.run(app,host='localhost',port=8000)
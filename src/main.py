from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

from src.config import Config

app = FastAPI(
    title=Config.APP.TITLE,
    description=Config.APP.DESCRIPTION,
    version=Config.APP.VERSION,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=HTMLResponse)
async def root() -> HTMLResponse:
    html_content = """
    <html>
        <head>
            <title>Polynomial Arithmetic Calculator</title>
        </head>
        <body>
            <h1>Polynomial Arithmetic Calculator</h1>
            <p>Welcome to the Polynomial Arithmetic Calculator API</p>
        </body>
    </html>
    """

    return HTMLResponse(content=html_content, status_code=status.HTTP_200_OK)

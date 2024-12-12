from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

from src.config import Config
from src.controller import services_router, status_router

app = FastAPI(
    title=Config.APP.TITLE,
    description=Config.APP.DESCRIPTION,
    version=Config.APP.VERSION,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8001", "http://127.0.0.1:8001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(status_router)
app.include_router(services_router)


@app.get("/", response_class=HTMLResponse)
async def root() -> HTMLResponse:
    """
    Root endpoint that returns a simple HTML response.

    Returns:
        HTMLResponse: A simple HTML page with a welcome message.
    """
    html_content = """
    <html>
        <head>
            <title>Polynomial Arithmetic in GF Calculator API</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    padding: 20px;
                }
                h1 {
                    color: #333;
                }
                p {
                    color: #666;
                }
                a {
                    color: #06f;
                }
            </style>
        </head>
        <body>
            <h1>Welcome to the Galois Field Polynomials Calculator API</h1>
            <p>To access the docs, visit <a href="/docs">docs</a> or <a href="/redoc">redoc</a></p>
        </body>
    </html>
    """

    return HTMLResponse(content=html_content, status_code=status.HTTP_200_OK)

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import httpx

app = FastAPI(title="CodeForge Learning API",
              description="API for CodeForge Learning", version="1.0.0", docs_url="/api-docs", redoc_url="/reference", openapi_url="/schema.json", debug=True)


class User(BaseModel):
    name: str
    email: str
    password: str


@app.get("/")
async def root():
    return {"message": "Hello World from FastAPI"}


@app.get('/health')
async def get_health():
    return {"status": "OK"}


@app.get('/articles', summary="Get all articles", description="Returns a list of all articles", tags=["articles"])
async def articles():
    articles = [
        {
            "id": 1,
            "title": "Learning FastAPI",
            "category": "Technology"
        },
        {
            "id": 2,
            "title": "Understanding PostgreSQL",
            "category": "Database"
        },
        {
            "id": 3,
            "title": "Introduction to Redis",
            "category": "Backend"
        }
    ]

    return {"success": True, "data": articles}


@app.post('/articles', summary="Create an article", description="Create an article", tags=["articles"], status_code=201)
async def create_article():
    return {"success": True, "data": []}


@app.get('/external-data')
async def external_data():
    url = "https://jsonplaceholder.typicode.com/todos/1"

    async with httpx.AsyncClient() as client:
        data = await client.get(url)

    return data.json()


@app.get('/custom-response')
def custom_response():
    return JSONResponse(content={"success": True, "data": []}, status_code=201, headers={"X-Custom-Header": "Custom Header"}, media_type="application/json")


@app.post('/users')
async def create_user(user: User):
    return user

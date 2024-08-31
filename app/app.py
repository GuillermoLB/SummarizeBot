from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from app.scraper import scrape_article
from app.summarizer import generate_summary

app = FastAPI()

# Set up the templates directory
templates = Jinja2Templates(directory="templates")

# Serve static files from the "static" directory
app.mount("/static", StaticFiles(directory="static"), name="static")

class URLItem(BaseModel):
    url: str

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/summarize/")
async def summarize(url_item: URLItem):
    article_data = scrape_article(url_item.url)
    if not article_data['content']:
        raise HTTPException(status_code=404, detail="Article content not found")
    summary = generate_summary(article_data['content'])
    return {"title": article_data['title'], "summary": summary}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)

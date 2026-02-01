from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Mount static first to ensure the breathing CSS loads instantly
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_welcome(request: Request):
    return templates.TemplateResponse("index1.html", {"request": request})

@app.get("/dashboard", response_class=HTMLResponse)
async def read_dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.get("/portal-selection", response_class=HTMLResponse)
async def read_portal_selection(request: Request):
    return templates.TemplateResponse("portal_selection.html", {"request": request})

@app.get("/portal/register", response_class=HTMLResponse)
async def read_signup(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})

@app.post("/complete-registration")
async def handle_registration(request: Request):
    form_data = await request.form()
    return {"status": "received", "role": form_data.get("role")}
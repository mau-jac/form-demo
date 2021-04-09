from typing import Optional
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from utils import add_user_db

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


fake_db = [{"name": "Foo Bar", "email": "foo@gmail.com", "password": "1234bad"}]


@app.get("/", response_class=HTMLResponse)
def read_item(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})


@app.get("/submit/")
def create_item(request: Request, name: str, password: str, new_email: str,):

    add_user_db(fake_db, name, new_email, password)

    return templates.TemplateResponse(
        "confirm.html", {
            "request": request,
            "method": "GET",
            "name": name,
            "password": password,
            "email": new_email
        })


@app.post("/submit/")
def create_secure_item(request: Request,
                       name: str = Form(...),
                       password: str = Form(...),
                       new_email: str = Form(...)):
    return templates.TemplateResponse(
        "confirm.html", {
            "request": request,
            "method": "POST",
            "name": name,
            "password": password,
            "email": new_email
        })


@app.get("/users/")
def list_users(request: Request):
    return templates.TemplateResponse(
        "users.html", {"request": request, "users": fake_db })
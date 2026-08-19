from fastapi import FastAPI
from .database import sessionLocal

from .models import Case
from .models import Motherboard
from .models import RAM
from .models import CPU
from .models import GPU
from .models import Storage
from .models import CPUCooler
from .models import PSU

app = FastAPI()

@app.get("/")
def home():
    return {"message" : "Connected"}

@app.get("/cases")
def get_parts():
    db = sessionLocal()
    result = db.query(Case).all()
    cases = []

    for case in result:
        cases.append({
            "id":case.id,
            "brand":case.brand,
            "model":case.model,
            "form_factor":case.form_factor
        })
    db.close()

    return cases

@app.get("/motherboards")
def get_parts():
    db = sessionLocal()
    result = db.query(Motherboard).all()
    mbs = []

    for mb in result:
        mbs.append({
            "id":mb.id,
            "brand":mb.brand,
            "model":mb.model,
            "form_factor":mb.form_factor
        })
    db.close()

    return mbs

@app.get("/cpus")
def get_parts():
    db = sessionLocal()
    result = db.query(CPU).all()
    cpus = []

    for cpu in result:
        cpus.append({
            "id":cpu.id,
            "brand":cpu.brand,
            "model":cpu.model
        })
    db.close()

    return cpus

@app.get("/rams")
def get_parts():
    db = sessionLocal()
    result = db.query(RAM).all()
    rams = []

    for ram in result:
        rams.append({
            "id":ram.id,
            "brand":ram.brand,
            "model":ram.model,
            "ram_type":ram.ram_type
        })
    db.close()

    return rams

@app.get("/gpus")
def get_parts():
    db = sessionLocal()
    result = db.query(GPU).all()
    gpus = []

    for gpu in result:
        gpus.append({
            "id":gpu.id,
            "brand":gpu.brand,
            "model":gpu.model,
        })
    db.close()

    return gpus

@app.get("/storage")
def get_parts():
    db = sessionLocal()
    result = db.query(Storage).all()
    storages = []

    for storage in result:
        storages.append({
            "id":storage.id,
            "brand":storage.brand,
            "model":storage.model,
            "storage_type":storage.storage_type
        })
    db.close()

    return storages

@app.get("/cooler")
def get_parts():
    db = sessionLocal()
    result = db.query(CPUCooler).all()
    coolers = []

    for cooler in result:
        coolers.append({
            "id":cooler.id,
            "brand":cooler.brand,
            "model":cooler.model,
        })
    db.close()

    return coolers

@app.get("/psu")
def get_parts():
    db = sessionLocal()
    result = db.query(PSU).all()
    psus = []

    for psu in result:
        psus.append({
            "id":psu.id,
            "brand":psu.brand,
            "model":psu.model,
        })
    db.close()

    return psus
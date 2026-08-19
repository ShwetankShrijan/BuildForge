from pydantic import BaseModel

class PCSelection(BaseModel):
    case_id: int
    motherboard_id: int
    cpu_id: int
    ram_id: int
    gpu_id: int
    storage_id: int
    cooler_id: int
    psu_id: int
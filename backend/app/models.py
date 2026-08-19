from sqlalchemy import Column, Integer, String
from .database import Base

class Case(Base):
    __tablename__ = "cases"

    id = Column(Integer, primary_key=True)
    form_factor = Column(String(20), nullable=False)
    height = Column(Integer, nullable=False)
    width = Column(Integer, nullable=False)
    length = Column(Integer, nullable=False)
    max_cooler_height = Column(Integer, nullable=False)
    max_gpu_height = Column(Integer, nullable=False)
    max_gpu_width = Column(Integer, nullable=False)
    max_gpu_length = Column(Integer, nullable=False)
    psu_support = Column(String(20), nullable=False)
    brand = Column(String(50))
    model = Column(String(100))

class Motherboard(Base):
    __tablename__ = "motherboards"

    id = Column(Integer, primary_key=True)
    form_factor = Column(String(20), nullable=False)
    socket = Column(String(20), nullable=False)
    chipset = Column(String(20), nullable=False)
    expansion_slot = Column(String(20), nullable=False)
    ram_type = Column(String(20), nullable=False)
    ram_slot_count = Column(Integer, nullable=False)
    bios = Column(String(20), nullable=False)
    m2_slots = Column(Integer)
    sata_ports = Column(Integer)
    brand = Column(String(50))
    model = Column(String(100))

class RAM(Base):
    __tablename__ = "rams"

    id = Column(Integer, primary_key=True)
    form_factor = Column(String(20), nullable=False)
    ram_type = Column(String(20), nullable=False)
    count = Column(Integer, nullable=False)
    ram_size_gb = Column(Integer, nullable=False)
    brand = Column(String(50))
    model = Column(String(100))

class CPU(Base):
    __tablename__ = "cpus"

    id = Column(Integer, primary_key=True)
    cores = Column(Integer, nullable=False)
    threads = Column(Integer, nullable=False)
    socket = Column(String(20), nullable=False)
    bios = Column(String(20), nullable=False)
    tdp = Column(Integer, nullable=False)
    brand = Column(String(50))
    model = Column(String(100))

class GPU(Base):
    __tablename__ = "gpus"

    id = Column(Integer, primary_key=True)
    height = Column(Integer, nullable=False)
    width = Column(Integer, nullable=False)
    length = Column(Integer, nullable=False)
    pcie_interface = Column(String(20), nullable=False)
    pcie_generation = Column(String(20), nullable=False)
    power_req = Column(Integer, nullable=False)
    power_connectors = Column(String(20), nullable=False)
    brand = Column(String(50))
    model = Column(String(100))

class Storage(Base):
    __tablename__ = "storages"

    id = Column(Integer, primary_key=True)
    storage_type = Column(String(20))
    interface = Column(String(30))
    capacity_gb = Column(Integer)
    form_factor = Column(String(20))
    brand = Column(String(50))
    model = Column(String(100))

class CPUCooler(Base):
    __tablename__ = "cpu_coolers"

    id = Column(Integer, primary_key=True)
    cooler_type = Column(String(20))
    socket_support = Column(String(50))
    height = Column(Integer)
    tdp_rating = Column(Integer)
    brand = Column(String(50))
    model = Column(String(100))

class PSU(Base):
    __tablename__ = "psus"

    id = Column(Integer, primary_key=True)
    wattage = Column(Integer)
    efficiency_rating = Column(String(20))
    form_factor = Column(String(20))
    pcie_connectors = Column(Integer)
    brand = Column(String(50))
    model = Column(String(100))
from .models import Case,Motherboard,RAM,CPU,GPU,Storage,CPUCooler,PSU

def check_case_motherboard(Case, Motherboard):
    if Case.form_factor == "ATX":
        return True
    elif Case.form_factor == Motherboard.form_factor:
        return True
    return False

def check_cpu_motherboard(CPU, Motherboard):
    if CPU.socket == Motherboard.socket and CPU.bios == Motherboard.bios:
        return True
    return False

def check_ram_motherboard(RAM, Motherboard):
    if RAM.ram_type == Motherboard.ram_type:
        if RAM.count <= Motherboard.ram_slot_count:
            return True
    return False

def check_gpu_case(gpu, case):
    if gpu.height <= case.max_gpu_height:
        if gpu.width <= case.max_gpu_width:
            if gpu.length <= case.max_gpu_length:
                return True
    return False

def check_gpu_motherboard(gpu, motherboard):
    if gpu.pcie_interface == motherboard.expansion_slot:
        return True
    return False

def check_storage_motherboard(storage, motherboard):
    if storage.storage_type == motherboard.expansion_slot:
        return True
    return False

def check_cooler_cpu(cooler, cpu):
    if cooler.socket_support == cpu.socket:
        if cooler.tdp_rating >= cpu.tdp:
            return True
    return False

def check_cooler_case(cooler, case):
    if cooler.height <= case.max_cooler_height:
        return True
    return False

def check_psu_case(psu, case):
    if psu.form_factor == case.psu_support:
        return True
    return False

def check_psu_gpu(psu, gpu):
    if psu.pcie_connectors >= gpu.power_connectors:
        return True
    return False
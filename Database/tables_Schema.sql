CREATE TABLE cases (
	id SERIAL PRIMARY KEY,
	form_factor VARCHAR(20) NOT NULL,
	height INT NOT NULL,
	width INT NOT NULL,
	length INT NOT NULL,
	max_cooler_height INT NOT NULL,
	max_gpu_height INT NOT NULL,
	max_gpu_width INT NOT NULL,
	max_gpu_length INT NOT NULL,
	psu_support VARCHAR(20) NOT NULL
);

CREATE TABLE motherboards (
	id SERIAL PRIMARY KEY,
	form_factor VARCHAR(20) NOT NULL,
	socket VARCHAR(20) NOT NULL,
	chipset VARCHAR(20) NOT NULL,
	expansion_slot VARCHAR(20) NOT NULL,
	ram_type VARCHAR(20) NOT NULL,
	ram_slot_count INT NOT NULL,
	bios VARCHAR(20) NOT NULL,
	m2_slots int,
	sata_ports int 	
);

CREATE TABLE rams (
	id SERIAL PRIMARY KEY,
	form_factor VARCHAR(20) NOT NULL,
	ram_type VARCHAR(20) NOT NULL,
	count INT NOT NULL,
	ram_size_gb INT NOT NULL
);

CREATE TABLE cpus (
	id SERIAL PRIMARY KEY,
	cores INT NOT NULL,
	threads INT NOT NULL,
	socket VARCHAR(20) NOT NULL,
	bios VARCHAR(20) NOT NULL,
	tdp int NOT NULL	
);

CREATE TABLE gpus (
	id SERIAL PRIMARY KEY,
	height INT NOT NULL,
	width INT NOT NULL,
	length INT NOT NULL,
 	pcie_interface varchar(20) NOT NULL,
  	pcie_generation varchar(20) NOT NULL,
  	power_req INT NOT NULL,
  	power_connectors INT NOT NULL	
);

CREATE TABLE storages (
  id SERIAL PRIMARY KEY,
  storage_type VARCHAR(20),
  interface VARCHAR(30),
  capacity_gb INT,
  form_factor VARCHAR(20)
);

CREATE TABLE cpu_coolers (
  id SERIAL PRIMARY KEY,
  cooler_type VARCHAR(20),
  socket_support VARCHAR(50),
  height INT,
  tdp_rating INT
);

CREATE TABLE psus (
  id SERIAL PRIMARY KEY,
  wattage INT,
  efficiency_rating VARCHAR(20),
  form_factor VARCHAR(20),
  pcie_connectors INT
);
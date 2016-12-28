--Users table
drop table if exists user;
create table user (
  user_id integer primary key autoincrement,
  user_name text not null,
  user_password text not null
);
--Basic info about an item
drop table if exists item;
create table item (
  item_id integer primary key autoincrement,
  item_name text,
  item_subtitle text,
  item_desc text,
  item_category text,
  item_condition text,
  item_conditionDesc text,
  item_cost numeric,
  item_returnPolicyDesc text,
  item_insertDate datetime
);

--Item Condition for a particular item
drop table if exists itemCondition;
create table itemCondition (
  itemCondition_id integer primary key autoincrement,
  itemCondition_name text
);
--Shipping info for a particular item
drop table if exists itemShipping;
create table itemShipping (
  itemShipping_id integer primary key autoincrement,
  itemShipping_method text,
  itemShipping_weight numeric,
  itemShipping_boxType text,
  itemShipping_boxWidth numeric,
  itemShipping_boxHeight numeric,
  itemShipping_boxLength numeric,
  itemShipping_handlingDuration datetime,
  itemShipping_itemLocation text,
  itemShipping_item_id integer,
  FOREIGN KEY(itemShipping_item_id) REFERENCES item(item_id)
);
--Pictures for a particular item
drop table if exists itemPicture;
create table itemPicture (
  itemPicture_id integer primary key autoincrement,
  itemPicture_data blob,
  itemPicture_caption text,
  itemPicture_item_id integer,
  FOREIGN KEY(itemPicture_item_id) REFERENCES item(item_id)
);
--Metrics for a particular item (will need to allow for adding new specs on the fly)
drop table if exists itemSpecs;
create table itemSpecs (
  itemSpecs_id integer primary key autoincrement,
  itemSpecs_name text,
  itemSpecs_value text,
  itemSpecs_item_id integer,
  FOREIGN KEY(itemSpecs_item_id) REFERENCES item(item_id)
);
--Ebay-specific Item Data
drop table if exists itemEbay;
create table itemEbay (
  itemEbay_id integer primary key autoincrement,
  itemEbay_bid text,
  itemEbay_buyItNow numeric,
  itemEbay_reservePrice numeric,
  itemEbay_fpQuantity integer,
  itemEbay_fpBestOffer numeric,
  itemEbay_fpMin numeric,
  itemEbay_fpMax numeric,
  itemEbay_duration datetime,
  itemEbay_insertionFee numeric,
  itemEbay_tax numeric,
  itemEbay_item_id integer,
  FOREIGN KEY(itemEbay_item_id) REFERENCES item(item_id)
);
--Table of PC Builds
drop table if exists pcBuild;
create table pcBuild (
  pcBuild_id integer primary key autoincrement,
  pcBuild_name text,
  pcBuild_type text,
  pcBuild_notes text,
  pcBuild_avgPartAge numeric,
  pcBuild_mobo_id integer,
  pcBuild_case_id integer,
  pcBuild_ram_id integer,
  pcBuild_gpu_id integer,
  pcBuild_ssd_id integer,
  pcBuild_hdd_id integer,
  pcBuild_cpu_id integer,
  pcBuild_psu_id integer,
  pcBuild_cpuCool_id integer,
  pcBuild_fan_id integer,
  pcBuild_ledkit_id integer,
  pcBuild_os_id integer,
  pcBuild_colorScheme text
);
--General PC Part Info
drop table if exists pcPart;
create table pcPart (
  pcPart_id integer primary key autoincrement,
  pcPart_type text,
  pcPart_name text,
  pcPart_modelNumber text,
  pcPart_price numeric,
  pcPart_desc text,
  pcPart_brand text,
  pcPart_condition text,
  pcPart_notes text,
  pcPart_age integer,
  pcPart_pcBuild_id,
  FOREIGN KEY(pcPart_pcBuild_id) REFERENCES pcBuild(pcBuild_id)
);
--RAM Part-Specific Info
drop table if exists ram;
create table ram (
  ram_id integer primary key autoincrement,
  ram_kitSize text,
  ram_stickSize integer,
  ram_speed integer,
  ram_type text,
  ram_casLatency text,
  ram_pcPart_id integer,
  ram_pcBuild_id integer,
  FOREIGN KEY(ram_pcPart_id) REFERENCES pcPart(pcPart_id),
  FOREIGN KEY(ram_pcBuild_id) REFERENCES pcBuild(pcBuild_id)
);
--Solid State Drive Part-Specific Info
drop table if exists ssd;
create table ssd (
  ssd_id integer primary key autoincrement,
  ssd_formFactor text,
  ssd_size integer,
  ssd_interface text,
  ssd_pcPart_id integer,
  ssd_pcBuild_id integer,
  FOREIGN KEY(ssd_pcPart_id) REFERENCES pcPart(pcPart_id),
  FOREIGN KEY(ssd_pcBuild_id) REFERENCES pcBuild(pcBuild_id)
);

--HDD Part-Specific Info
drop table if exists hdd;
create table hdd (
  hdd_id integer primary key autoincrement,
  hdd_formFactor text,
  hdd_size integer,
  hdd_interface text,
  hdd_cache integer,
  hdd_rpm integer,
  hdd_pcPart_id integer,
  hdd_pcBuild_id integer,
  FOREIGN KEY(hdd_pcPart_id) REFERENCES pcPart(pcPart_id),
  FOREIGN KEY(hdd_pcBuild_id) REFERENCES pcBuild(pcBuild_id)
);
--Case Part-Specific Info
drop table if exists cases;
create table cases (
  case_id integer primary key autoincrement,
  case_formFactor text,
  case_width numeric,
  case_height numeric,
  case_length numeric,
  case_525bay integer,
  case_350bay integer,
  case_250bay integer,
  case_80fan integer,
  case_120fan integer,
  case_140fan integer,
  case_240fan integer,
  case_otherFan text,
  case_fpSpk integer,
  case_fpMic integer,
  case_fpUSB3 integer,
  case_fpUSB2 integer,
  case_psuSlots integer,
  case_waterSlots text,
  case_pcPart_id integer,
  case_pcBuild_id integer,
  FOREIGN KEY(case_pcPart_id) REFERENCES pcPart(pcPart_id),
  FOREIGN KEY(case_pcBuild_id) REFERENCES pcBuild(pcBuild_id)
);
--Video Card Part-Specific Info
drop table if exists gpu;
create table gpu (
  gpu_id integer primary key autoincrement,
  gpu_vramType text,
  gpu_vramSize text,
  gpu_slotWidth text,
  gpu_interface text,
  gpu_6pin integer,
  gpu_8pin integer,
  gpu_clockSpeed numeric,
  gpu_memClockSpeed numeric,
  gpu_busBandwidth numeric,
  gpu_crossfire integer,
  gpu_sli integer,
  gpu_pcPart_id integer,
  gpu_pcBuild_id integer,
  FOREIGN KEY(gpu_pcPart_id) REFERENCES pcPart(pcPart_id),
  FOREIGN KEY(gpu_pcBuild_id) REFERENCES pcBuild(pcBuild_id)
);
--Power Supply Part-Specific Info
drop table if exists psu;
create table psu (
  psu_id integer primary key autoincrement,
  psu_watt integer,
  psu_effiency text,
  psu_8pin integer,
  psu_6pin integer,
  psu_4pin integer,
  psu_molex integer,
  psu_sata integer,
  psu_floppy integer,
  psu_pcPart_id integer,
  psu_pcBuild_id integer,
  FOREIGN KEY(psu_pcPart_id) REFERENCES pcPart(pcPart_id),
  FOREIGN KEY(psu_pcBuild_id) REFERENCES pcBuild(pcBuild_id)
);
--Operating System Part-Specific Info
drop table if exists os;
create table os (
  os_id integer primary key autoincrement,
  os_type text,
  os_bit integer,
  os_version text,
  os_pcPart_id text,
  os_pcBuild_id integer,
  FOREIGN KEY(os_pcPart_id) REFERENCES pcPart(pcPart_id),
  FOREIGN KEY(os_pcBuild_id) REFERENCES pcBuild(pcBuild_id)
);
--CPU Cooler Part-Specific Info
drop table if exists cpuCool;
create table cpuCool (
  cpuCool_id integer primary key autoincrement,
  cpuCool_type text,
  cpuCool_socketList text,
  cpuCool_fanCount integer,
  cpuCool_fanSize text,
  cpuCool_pcPart_id integer,
  cpuCool_pcBuild_id integer,
  FOREIGN KEY(cpuCool_pcPart_id) REFERENCES pcPart(pcPart_id),
  FOREIGN KEY(cpuCool_pcBuild_id) REFERENCES pcBuild(pcBuild_id)
);
--Motherboard Part-Specific Info
drop table if exists mobo;
create table mobo (
  mobo_id integer primary key autoincrement,
  mobo_ramType text,
  mobo_CPUsocket text,
  mobo_dimmSlots integer,
  mobo_pciSlots integer,
  mobo_pcie16Slots integer,
  mobo_pcie8Slots integer,
  mobo_pcie4Slots integer,
  mobo_pcie1Slots integer,
  mobo_chipset text,
  mobo_cpu4pin integer,
  mobo_cpu8pin integer,
  mobo_cpu6pin integer,
  mobo_pcPart_id integer,
  mobo_pcBuild_id integer,
  FOREIGN KEY(mobo_pcPart_id) REFERENCES pcPart(pcPart_id),
  FOREIGN KEY(mobo_pcBuild_id) REFERENCES pcBuild(pcBuild_id)
);
--Case Fans Part-Specific Info
drop table if exists fan;
create table fan (
  fan_id integer primary key autoincrement,
  fan_size integer,
  fan_type text,
  fan_color text,
  fan_pcPart_id integer,
  fan_pcBuild_id integer,
  FOREIGN KEY(fan_pcPart_id) REFERENCES pcPart(pcPart_id),
  FOREIGN KEY(fan_pcBuild_id) REFERENCES pcBuild(pcBuild_id)
);
--LED Kits Part-Specific Info
drop table if exists ledkit;
create table ledkit (
  ledkit_id integer primary key autoincrement,
  ledkit_color text,
  ledkit_type text,
  ledkit_notes text,
  ledkit_pcPart_id integer,
  ledkit_pcBuild_id integer,
  FOREIGN KEY(ledkit_pcPart_id) REFERENCES pcPart(pcPart_id),
  FOREIGN KEY(ledkit_pcBuild_id) REFERENCES pcBuild(pcBuild_id)
);
--CPU Part-Specific Info
drop table if exists cpu;
create table cpu (
  cpu_id integer primary key autoincrement,
  cpu_socket text,
  cpu_cores integer,
  cpu_threads integer,
  cpu_frequency numeric,
  cpu_cache integer,
  cpu_wattage integer,
  cpu_pcParts_id integer,
  cpu_pcBuild_id integer,
  FOREIGN KEY(cpu_pcParts_id) REFERENCES pcPart(pcPart_id),
  FOREIGN KEY(cpu_pcBuild_id) REFERENCES pcBuild(pcBuild_id)
);



--Benchmark general data for a particular PC
drop table if exists pcBenchmark;
create table pcBenchmark (
  pcBenchmark_id integer primary key autoincrement,
  pcBenchmark_notes text,
  pcBenchmark_score text,
  pcBenchmark_fps text,
  pcBenchmark_pcBuild_id integer,
  FOREIGN KEY(pcBenchmark_pcBuild_id) REFERENCES pcBuild(pcBuild_id)
);

--Picture storage for a particular PC's benchmarks
drop table if exists pcBenchmarkPictures;
create table pcBenchmarkPictures (
  pcBenchmarkPictures_id integer primary key autoincrement,
  pcBenchmarkPictures_data blob,
  pcBenchmarkPictures_pcBenchmark_id integer,
  FOREIGN KEY(pcBenchmarkPictures_pcBenchmark_id) REFERENCES pcBenchmark(pcBenchmark_id)
);

--List of applications / games available for selection
drop table if exists benchmarkAppList;
create table benchmarkAppList (
  benchmarkAppList_id integer primary key autoincrement,
  --Type: either game or non-game
  benchmarkAppList_type text,
  benchmarkAppList_name text
);



INSERT INTO user 
        (user_name, 
        user_password) 
        VALUES ("admin",
                "testing");
INSERT INTO pcPart 
        (pcPart_type, 
        pcPart_name, 
        pcPart_modelNumber) 
        VALUES ("psu",
                "Antec 500W",
                "AN500W");
INSERT INTO psu 
        (psu_watt, 
        psu_effiency, 
        psu_pcPart_id) 
        VALUES (500,
                "80plus",
                1);
                
                
INSERT INTO pcPart 
        (pcPart_type, 
        pcPart_name, 
        pcPart_modelNumber) 
        VALUES ("psu",
                "Thermaltake 750W",
                "TT750W");
INSERT INTO psu 
        (psu_watt, 
        psu_effiency, 
        psu_pcPart_id) 
        VALUES (750,
                "titanium",
                2);
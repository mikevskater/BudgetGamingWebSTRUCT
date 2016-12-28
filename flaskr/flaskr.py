# all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

""" ---------------- ---------------- App Init ---------------- ---------------- """
# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='testing'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

""" ---------------- ---------------- Database Functions ---------------- ---------------- """
def connect_db():
    #Connects to the specific database
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    #Opens a new database connection if there is none yet for the current application context
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    #Closes the database again at the end of the request
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    #db.execute('PRAGMA FOREIGN_KEYS=ON')
    #db.execute('PRAGMA foreign_keys  = "1"')
    db.commit()

@app.cli.command('initdb')
def initdb_command():
    #Initializes the database
    init_db()
    print 'Initialized the database.'


""" ---------------- ---------------- General Functions ---------------- ---------------- """
#Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            
            return redirect(url_for('item_list'))
    return render_template('login.html', error=error)

#Logout
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('item_list'))

#Upload
@app.route("/upload", methods=["POST"])
def upload():
    uploaded_files = flask.request.files.getlist("file[]")
    print uploaded_files
    return ""
    
#Get row count of a table
def get_next_row(currentTable):
    sql_string = open('sql/select_row_count.sql', 'r').read()
    sql_string = sql_string.replace("currentTable", currentTable)
    db = get_db()
    cur = db.execute(sql_string)
    row_count = cur.fetchone()
    return row_count
    
""" ---------------- ---------------- Main Routes ---------------- ---------------- """
#Display Data - Dashboard
@app.route('/')
def dashboard():
    return render_template('dashboard.html')
    
""" ---------------- ---------------- List Parts ---------------- ---------------- """
#Select all parts and display webpage
@app.route('/pcparts_list')
def pcparts_list():
        sql_string = open('sql/select_all_pcparts.sql', 'r').read()
        db = get_db()
        cur = db.execute(sql_string)
        items = cur.fetchall()
        abc = db.execute('PRAGMA foreign_keys')
        abcX = abc.fetchall()
        print "FOREIGN KEY STATUS:"
        print abcX
        print "-----------------------"
        abc = db.execute('PRAGMA foreign_keys=ON')
        abc = db.execute('PRAGMA foreign_keys')
        abcY = abc.fetchall()
        print "FOREIGN KEY STATUS:"
        print abcY
        print "-----------------------"
        #Display the page
        #   items ==> list of columns and respective rows for all PC parts
        return render_template('pcparts_list.html', items=items)
        
        
#Select all builds and display webpage
@app.route('/pcparts_listBuilds')
def pcparts_listBuilds():
        #Select all builds
        pcBuildList = get_pcBuildList()
        #Display the page
        #   pcBuildList ==> list of columns and respective rows for all PC builds
        return render_template('pcparts_listBuilds.html', pcBuildList=pcBuildList)
        
#Get a part
def get_part(pcPartId):
        sql_string = open('sql/select_part.sql', 'r').read()
        db = get_db()
        abc = db.execute('PRAGMA foreign_keys=ON')
        cur = db.execute(sql_string, [pcPartId])
        part_row = cur.fetchone()
        #Return row of part details
        return part_row
        
        
#Get a part's details
def get_part_details(pcPartId):
        sql_string = open('sql/select_part_details.sql', 'r').read()
        db = get_db()
        abc = db.execute('PRAGMA foreign_keys=ON')
        cur = db.execute(sql_string, [pcPartId])
        part_details_row = cur.fetchone()
        #Return row of part details
        return part_details_row

#Display Data - a part's details
@app.route('/pcparts_list/<int:pcPartId>/part_details/')
def part_details(pcPartId):
        selected_row = get_part_details(pcPartId)
        #Display the page
        #   pcPartId ==> current part id
        #   selected_row ==> the part's details
        return render_template('/pcparts/select_ssd.html', pcPartId=pcPartId, selected_row=selected_row)
        
def fetch_parts():
        db = get_db()
        abc = db.execute('PRAGMA foreign_keys=ON')
        
        #Fetch Mobo List
        sql_string = open('sql/select_moboList.sql', 'r').read()
        result = db.execute(sql_string)
        moboList = result.fetchall()
        
        #Fetch Case List
        sql_string = open('sql/select_caseList.sql', 'r').read()
        result = db.execute(sql_string)
        caseList = result.fetchall()
        
        #Fetch PSU List
        sql_string = open('sql/select_psuList.sql', 'r').read()
        result = db.execute(sql_string)
        psuList = result.fetchall()
        
        #Fetch RAM List
        sql_string = open('sql/select_ramList.sql', 'r').read()
        result = db.execute(sql_string)
        ramList = result.fetchall()
        
        #Fetch GPU List
        sql_string = open('sql/select_gpuList.sql', 'r').read()
        result = db.execute(sql_string)
        gpuList = result.fetchall()
        
        #Fetch SSD List
        sql_string = open('sql/select_ssdList.sql', 'r').read()
        result = db.execute(sql_string)
        ssdList = result.fetchall()
        
        #Fetch HDD List
        sql_string = open('sql/select_hddList.sql', 'r').read()
        result = db.execute(sql_string)
        hddList = result.fetchall()
        
        #Fetch CPU List
        sql_string = open('sql/select_cpuList.sql', 'r').read()
        result = db.execute(sql_string)
        cpuList = result.fetchall()
        
        #Fetch CPU Cooling List
        sql_string = open('sql/select_cpuCoolList.sql', 'r').read()
        result = db.execute(sql_string)
        cpuCoolList = result.fetchall()
        
        #Fetch Fan List
        sql_string = open('sql/select_fanList.sql', 'r').read()
        result = db.execute(sql_string)
        fanList = result.fetchall()
        
        #Fetch LED Kit List
        sql_string = open('sql/select_ledkitList.sql', 'r').read()
        result = db.execute(sql_string)
        ledkitList = result.fetchall()
        
        #Fetch OS List
        sql_string = open('sql/select_osList.sql', 'r').read()
        result = db.execute(sql_string)
        osList = result.fetchall()
        
        dataList = []
        dataList.append(moboList)
        dataList.append(caseList)
        dataList.append(psuList)
        dataList.append(ramList)
        dataList.append(gpuList)
        dataList.append(ssdList)
        dataList.append(hddList)
        dataList.append(cpuList)
        dataList.append(cpuCoolList)
        dataList.append(fanList)
        dataList.append(ledkitList)
        dataList.append(osList)
        
        return dataList
        
        
        
#
#
# check out ebay API
# check out ebay API
# check out ebay API
# check out ebay API
#
#
""" ---------------- ---------------- PC Builds ---------------- ----------------"""
""" ---------------- Add PC Build  ----------------"""
#Display Form - Add a New Build
@app.route('/pcparts_addBuild.html', methods=['GET', 'POST'])
def pcparts_addBuild():
        db = get_db()
        abc = db.execute('PRAGMA foreign_keys=ON')
        
        #Fetch Mobo List
        sql_string = open('sql/select_moboList.sql', 'r').read()
        result = db.execute(sql_string)
        moboList = result.fetchall()
        
        #Fetch Case List
        sql_string = open('sql/select_caseList.sql', 'r').read()
        result = db.execute(sql_string)
        caseList = result.fetchall()
        
        #Fetch PSU List
        sql_string = open('sql/select_psuList.sql', 'r').read()
        result = db.execute(sql_string)
        psuList = result.fetchall()
        
        #Fetch RAM List
        sql_string = open('sql/select_ramList.sql', 'r').read()
        result = db.execute(sql_string)
        ramList = result.fetchall()
        
        #Fetch GPU List
        sql_string = open('sql/select_gpuList.sql', 'r').read()
        result = db.execute(sql_string)
        gpuList = result.fetchall()
        
        #Fetch SSD List
        sql_string = open('sql/select_ssdList.sql', 'r').read()
        result = db.execute(sql_string)
        ssdList = result.fetchall()
        
        #Fetch HDD List
        sql_string = open('sql/select_hddList.sql', 'r').read()
        result = db.execute(sql_string)
        hddList = result.fetchall()
        
        #Fetch CPU List
        sql_string = open('sql/select_cpuList.sql', 'r').read()
        result = db.execute(sql_string)
        cpuList = result.fetchall()
        
        #Fetch CPU Cooling List
        sql_string = open('sql/select_cpuCoolList.sql', 'r').read()
        result = db.execute(sql_string)
        cpuCoolList = result.fetchall()
        
        #Fetch Fan List
        sql_string = open('sql/select_fanList.sql', 'r').read()
        result = db.execute(sql_string)
        fanList = result.fetchall()
        
        #Fetch LED Kit List
        sql_string = open('sql/select_ledkitList.sql', 'r').read()
        result = db.execute(sql_string)
        ledkitList = result.fetchall()
        
        #Fetch OS List
        sql_string = open('sql/select_osList.sql', 'r').read()
        result = db.execute(sql_string)
        osList = result.fetchall()
        
        return render_template('pcparts_addBuild.html' moboList=moboList,
                caseList=caseList,
                psuList=psuList,
                ramList=ramList,
                gpuList=gpuList,
                ssdList=ssdList,
                hddList=hddList,
                cpuList=cpuList,
                cpuCoolList=cpuCoolList,
                fanList=fanList,
                ledkitList=ledkitList,
                osList=osList)
                
def get_pcBuildList():
        db = get_db()
        abc = db.execute('PRAGMA foreign_keys=ON')
        cur = db.execute('SELECT * FROM pcBuild')
        pcBuildList = pcBuildList.fetchall()
        return pcBuildList
    
#Submit POST - Add a New Build
@app.route('/pcpart_add_build', methods=['GET', 'POST'])
def add_build():
    if not session.get('logged_in'):
        abort(401)
        
    sql_string = open('sql/insert_build.sql', 'r').read()
    db = get_db()
    abc = db.execute('PRAGMA foreign_keys=ON')
    db.execute(sql_string, [request.form['pcBuild_name'], 
        request.form['pcBuild_type'], 
        request.form['pcBuild_notes'], 
        request.form['pcBuild_avgPartAge'], 
        request.form['pcBuild_mobo_id'], 
        request.form['pcBuild_case_id'], 
        request.form['pcBuild_ram_id'], 
        request.form['pcBuild_gpu_id'], 
        request.form['pcBuild_ssd_id'], 
        request.form['pcBuild_hdd_id'], 
        request.form['pcBuild_cpu_id'], 
        request.form['pcBuild_psu_id'], 
        request.form['pcBuild_cpuCool_id'], 
        request.form['pcBuild_fan_id'], 
        request.form['pcBuild_ledkit_id'], 
        request.form['pcBuild_os_id'], 
        request.form['pcBuild_colorScheme']])
    db.commit()
    
    return redirect(url_for('display_addPart_details'))


""" ---------------- ---------------- Add Part ---------------- ----------------"""
""" ---------------- Add Part - Generic ----------------"""
#Display Form - Add a New Part
@app.route('/pcparts_addPart.html', methods=['GET', 'POST'])
def pcparts_addPart():
    return render_template('pcparts_addPart.html') 
    
#Submit POST - Add a New Part
@app.route('/pcpart_add_part', methods=['GET', 'POST'])
def add_part():
    if not session.get('logged_in'):
        abort(401)
        
    sql_string = open('sql/insert_part.sql', 'r').read()
    request_string = ""
    db = get_db()
    abc = db.execute('PRAGMA foreign_keys=ON')
    db.execute(sql_string, [request.form['pcPart_type'], 
        request.form['pcPart_name'], 
        request.form['pcPart_modelNumber'], 
        request.form['pcPart_price'], 
        request.form['pcPart_desc'], 
        request.form['pcPart_brand'], 
        request.form['pcPart_condition'], 
        request.form['pcPart_notes'], 
        request.form['pcPart_test'], 
        request.form['pcPart_age']])
    db.commit()
    
    #return redirect(url_for('pcparts_addPart_ssd'))
    return redirect(url_for('display_addPart_details'))
    
""" ---------------- Add Part - Specific ----------------"""

#Display Form - Add Part Details - Generic
@app.route('/display_addPart_details.html', methods=['GET', 'POST'])
def display_addPart_details():
    db = get_db()
    abc = db.execute('PRAGMA foreign_keys=ON')
    cur = db.execute('SELECT max(pcPart_id) FROM pcPart')
    maxRowCount = cur.fetchall()
    currentPart = maxRowCount[0][0]
    print "currentPart"
    print currentPart
    print "currentPart"
    sql_string = "SELECT pcPart_type FROM pcPart WHERE pcPart_id = currentPart"
    print "sql_string"
    print sql_string
    print "sql_string"
    sql_string = sql_string.replace("currentPart", str(currentPart))
    get_partType = db.execute(sql_string)
    partTypeX = get_partType.fetchone()
    partType = partTypeX[0]
    print "partType"
    print partType
    print "partType"
    pcBuildList = get_pcBuildList()
    return render_template('display_addPart_details.html', currentPart=currentPart, partType=partType, pcBuildList=pcBuildList)

#
#
#    return render_template('display_addPart_details.html', currentPart=currentPart, partType=partType, 
#        moboList=dataList[0], caseList=dataList[1], psuList=dataList[2],
#        ramList=dataList[3], gpuList=dataList[4], ssdList=dataList[5],
#        hddList=dataList[6], cpuList=dataList[7], cpuCoolList=dataList[8],
#        fanList=dataList[9], ledkitList=dataList[10], osList=dataList[11]
#
#


#Submit POST - Add a New Part Details - Generic
@app.route('/pcpart/add_part_details', methods=['POST'])
def add_part_details():
        if not session.get('logged_in'):
                abort(401)
        db = get_db()
        abc = db.execute('PRAGMA foreign_keys=ON')
        #SSD
        if request.form['part_type'] == "ssd":
                sql_string = open('sql/insert_ssd.sql', 'r').read()
                db.execute(sql_string,
                [request.form['ssd_formFactor'], 
                request.form['ssd_size'],
                request.form['ssd_interface'],
                request.form['pc_part_id'],
                request.form['pc_build_id']])
                db.commit()
                flash('New part was added to database!')
                return redirect(url_for('pcparts_list.html'))
        #RAM
        elif request.form['part_type'] == "ram":
                sql_string = open('sql/insert_ram.sql', 'r').read()
                db.execute(sql_string,
                [request.form['ram_kitSize'], 
                request.form['ram_stickSize'],
                request.form['ram_type'],
                request.form['ram_casLatency'],
                request.form['pc_part_id'],
                request.form['pc_build_id']])
                db.commit()
                flash('New part was added to database!')
                return redirect(url_for('pcparts_list.html'))
        #HDD
        elif request.form['part_type'] == "hdd":
                sql_string = open('sql/insert_hdd.sql', 'r').read()
                db.execute(sql_string,
                [request.form['hdd_formFactor'], 
                request.form['hdd_size'],
                request.form['hdd_interface'],
                request.form['hdd_cache'],
                request.form['hdd_rpm'],
                request.form['pc_part_id'],
                request.form['pc_build_id']])
                db.commit()
                flash('New part was added to database!')
                return redirect(url_for('pcparts_list.html'))
        #CASE
        elif request.form['part_type'] == "case":
                sql_string = open('sql/insert_case.sql', 'r').read()
                db.execute(sql_string,
                [request.form['case_formFactor'], 
                request.form['case_width'],
                request.form['case_height'],
                request.form['case_length'],
                request.form['case_525bay'],
                request.form['case_350bay'],
                request.form['case_250bay'],
                request.form['case_80fan'],
                request.form['case_120fan'],
                request.form['case_140fan'],
                request.form['case_240fan'],
                request.form['case_otherFan'],
                request.form['case_fpSpk'],
                request.form['case_fpMic'],
                request.form['case_fpUSB3'],
                request.form['case_fpUSB2'],
                request.form['case_psuSlots'],
                request.form['case_waterSlots'],
                request.form['pc_part_id'],
                request.form['pc_build_id']])
                db.commit()
                flash('New part was added to database!')
                return redirect(url_for('pcparts_list.html'))
        #GPU
        elif request.form['part_type'] == "gpu":
                sql_string = open('sql/insert_gpu.sql', 'r').read()
                db.execute(sql_string,
                [request.form['gpu_vramType'], 
                request.form['gpu_vramSize'],
                request.form['gpu_slotWidth'],
                request.form['gpu_interface'],
                request.form['gpu_6pin'],
                request.form['gpu_8pin'],
                request.form['gpu_clockSpeed'],
                request.form['gpu_memClockSpeed'],
                request.form['gpu_busBandwidth'],
                request.form['gpu_crossfire'],
                request.form['gpu_sli'],
                request.form['pc_part_id'],
                request.form['pc_build_id']])
                db.commit()
                flash('New part was added to database!')
                return redirect(url_for('pcparts_list.html'))
        #PSU
        elif request.form['part_type'] == "psu":
                sql_string = open('sql/insert_psu.sql', 'r').read()
                db.execute(sql_string,
                [request.form['psu_watt'], 
                request.form['psu_effiency'],
                request.form['psu_8pin'],
                request.form['psu_6pin'],
                request.form['psu_4pin'],
                request.form['psu_molex'],
                request.form['psu_sata'],
                request.form['psu_floppy'],
                request.form['pc_part_id'],
                request.form['pc_build_id']])
                db.commit()
                flash('New part was added to database!')
                return redirect(url_for('pcparts_list.html'))   
        #OS
        elif request.form['part_type'] == "os":
                sql_string = open('sql/insert_os.sql', 'r').read()
                db.execute(sql_string,
                [request.form['os_type'], 
                request.form['os_bit'],
                request.form['os_version'],
                request.form['pc_part_id'],
                request.form['pc_build_id']])
                db.commit()
                flash('New part was added to database!')
                return redirect(url_for('pcparts_list.html'))
        #CPU Cooler
        elif request.form['part_type'] == "cpuCool":
                sql_string = open('sql/insert_cpuCool.sql', 'r').read()
                db.execute(sql_string,
                [request.form['cpuCool_type'], 
                request.form['cpuCool_socketList'],
                request.form['cpuCool_fanCount'],
                request.form['cpuCool_fanSize'],
                request.form['pc_part_id'],
                request.form['pc_build_id']])
                db.commit()
                flash('New part was added to database!')
                return redirect(url_for('pcparts_list.html'))
        #Motherboard
        elif request.form['part_type'] == "mobo":
                sql_string = open('sql/insert_mobo.sql', 'r').read()
                db.execute(sql_string,
                [request.form['mobo_ramType'], 
                request.form['mobo_CPUsocket'],
                request.form['mobo_dimmSlots'],
                request.form['mobo_pciSlots'],
                request.form['mobo_pcie16Slots'],
                request.form['mobo_pcie8Slots'],
                request.form['mobo_pcie4Slots'],
                request.form['mobo_pcie1Slots'],
                request.form['mobo_chipset'],
                request.form['mobo_cpu4pin'],
                request.form['mobo_cpu8pin'],
                request.form['mobo_cpu6pin'],
                request.form['pc_part_id'],
                request.form['pc_build_id']])
                db.commit()
                flash('New part was added to database!')
                return redirect(url_for('pcparts_list.html'))
        #Fan
        elif request.form['part_type'] == "fan":
                sql_string = open('sql/insert_fan.sql', 'r').read()
                db.execute(sql_string,
                [request.form['fan_size'], 
                request.form['fan_type'],
                request.form['fan_color'],
                request.form['pc_part_id'],
                request.form['pc_build_id']])
                db.commit()
                flash('New part was added to database!')
                return redirect(url_for('pcparts_list.html'))
        #LED Kit
        elif request.form['part_type'] == "ledkit":
                sql_string = open('sql/insert_ledkit.sql', 'r').read()
                db.execute(sql_string,
                [request.form['ledkit_color'], 
                request.form['ledkit_type'],
                request.form['ledkit_notes'],
                request.form['pc_part_id'],
                request.form['pc_build_id']])
                db.commit()
                flash('New part was added to database!')
                return redirect(url_for('pcparts_list.html'))
        #Processor
        elif request.form['part_type'] == "cpu":
                sql_string = open('sql/insert_cpu.sql', 'r').read()
                db.execute(sql_string,
                [request.form['cpu_socket'], 
                request.form['cpu_cores'],
                request.form['cpu_threads'],
                request.form['cpu_frequency'],
                request.form['cpu_cache'],
                request.form['cpu_wattage'],
                request.form['pc_part_id'],
                request.form['pc_build_id']])
                db.commit()
                flash('New part was added to database!')
                return redirect(url_for('pcparts_list.html'))

#Display Form - Add Part Details - SSD
@app.route('/pcparts_add_ssd.html', methods=['GET', 'POST'])
def pcparts_addPart_ssd():
    currentTable = "pcPart"
    db = get_db()
    abc = db.execute('PRAGMA foreign_keys=ON')
    cur = db.execute('SELECT max(pcPart_id) FROM pcPart')
    maxRowCount = cur.fetchall()
    currentPart = maxRowCount[0][0]
    return render_template('pcparts_addPart_ssd.html', currentPart=currentPart)
    
#Submit POST - Add a New Part Details - SSD
@app.route('/pcpart/add_ssd', methods=['POST'])
def add_ssd():
    if not session.get('logged_in'):
        abort(401)
    sql_string = open('sql/insert_ssd.sql', 'r').read()
    db = get_db()
    abc = db.execute('PRAGMA foreign_keys=ON')
    db.execute(sql_string,
                 [request.form['ssd_formFactor'], 
                 request.form['ssd_size'],
                 request.form['ssd_interface'],
                 request.form['pc_part_id']])
    db.commit()
    flash('New part was added to database!')
    return redirect(url_for('dashboard'))


""" ---------------- ---------------- Update Part ---------------- ----------------"""
#Display Form - Update a part
@app.route('/pcparts/updatePart.html/', methods=['GET', 'POST'])
def display_update_part():
        sql_string = open('sql/update_part.sql', 'r').read()
        #db = get_db()
        #db.execute('PRAGMA FOREIGN_KEYS=ON')
        selected_row = get_part(request.form['part_to_update'])
        #partId_to_update = request.form['part_to_update']
        #Display the page
        #   partId_to_update ==> current part id to update
        #   selected_row ==> the part's details
        return render_template('/pcparts/updatePart.html', selected_row=selected_row)    
    

#Submit POST - Update a Part
@app.route('/pcparts/update_part', methods=['GET', 'POST'])
def update_part():
        if not session.get('logged_in'):
                abort(401)
        sql_string = open('sql/update_part.sql', 'r').read()
        db = get_db()
        abc = db.execute('PRAGMA foreign_keys=ON')
        db.execute(sql_string,[request.form['pcPart_type'], 
                request.form['pcPart_name'], 
                request.form['pcPart_modelNumber'], 
                request.form['pcPart_price'], 
                request.form['pcPart_desc'], 
                request.form['pcPart_brand'], 
                request.form['pcPart_condition'], 
                request.form['pcPart_notes'], 
                request.form['pcPart_test'], 
                request.form['pcPart_age'], 
                request.form['pcPart_id']])
        db.commit()
        flash('Part successfully updated!')
        return redirect(url_for('display_update_part_details', pcPartId=int(request.form['pcPart_id'])))


#Display Form - Update a part's details
@app.route('/pcparts/<int:pcPartId>/update_part_details.html', methods=['GET', 'POST'])
def display_update_part_details(pcPartId):
        selected_row = get_part_details(pcPartId)
        #Display the page
        #   pcPartId ==> current part id
        #   selected_row ==> the part's details
        return render_template('/pcparts/updatePart_details.html', selected_row=selected_row)    

#Submit POST - Update a Part's Details
@app.route('/pcparts/update_part_details/', methods=['GET', 'POST'])
def update_part_details():
        sql_string = open('sql/update_part_ssd.sql', 'r').read()
        #sql_string = sql_string.replace("pcPart_id", str(pcPartId))
        #part_table = "ssd"
        db = get_db()
        db.execute('PRAGMA FOREIGN_KEYS=ON')
        db.execute(sql_string,[ request.form['ssd_formFactor'],
                request.form['ssd_size'],
                request.form['ssd_interface'],
                request.form['ssd_pcPart_id']])
        #Display the page
        #   pcPartId ==> current part id
        #   selected_row ==> the part's details
        db.commit()
        flash('Part details successfully updated!')
        #return render_template('pcparts_list.html')
        return pcparts_list()
        
""" ---------------- ---------------- Delete Part ---------------- ----------------"""
@app.route('/delete_part', methods=['POST'])
def delete_part():
        sql_string = open('sql/delete_part.sql', 'r').read()
        db = get_db()
        db.execute('PRAGMA FOREIGN_KEYS=ON')
        db.execute(sql_string,[request.form['part_to_delete']])
        #db.execute('UPDATE SQLITE_SEQUENCE SET seq=0 WHERE NAME=\'pcPart\'')
        db.commit()
        flash('Part deleted from database!')
        return redirect(url_for('pcparts_list'))
        
        
""" ---------------- ---------------- List PC Parts ---------------- ---------------- """
@app.route('/pcparts/pcparts_ram')
def pcparts_ram():
    return render_template('pcparts_ram.html')   
    
@app.route('/pcparts/list_pcparts_ssd')
def list_pcparts_ssd():
    return render_template('list_pcparts_ssd.html')   
    
@app.route('/pcparts/pcparts_hdd')
def pcparts_hdd():
    return render_template('pcparts_hdd.html')   
    
@app.route('/pcparts/pcparts_case')
def pcparts_case():
    return render_template('pcparts_case.html')   
    
@app.route('/pcparts/pcparts_gpu')
def pcparts_gpu():
    return render_template('pcparts_gpu.html')   
    
@app.route('/pcparts/pcparts_psu')
def pcparts_psu():
    return render_template('pcparts_psu.html')   
    
@app.route('/pcparts/pcparts_os')
def pcparts_os():
    return render_template('pcparts_os.html')   
    
@app.route('/pcparts/pcparts_cpuCool')
def pcparts_cpuCool():
    return render_template('pcparts_cpuCool.html')   
    
@app.route('/pcparts/pcparts_mobo')
def pcparts_mobo():
    return render_template('pcparts_mobo.html')  
    
@app.route('/pcparts/pcparts_fan')
def pcparts_fan():
    return render_template('pcparts_fan.html')   
    
@app.route('/pcparts/pcparts_ledkit')
def pcparts_ledkit():
    return render_template('pcparts_ledkit.html')   
    
@app.route('/pcparts/pcparts_cpu')
def pcparts_cpu():
    return render_template('pcparts_cpu.html')  
    
#def pcparts_ssd():
    #print "OOOOOOOOOOOOOOOOOOOOOO"
    #print selected_row
    #print "OOOOOOOOOOOOOOOOOOOOOO"
    #print "PC PART ID: " + str(pcPartId) + " ---"
    #sql_string = open('select_ssd.sql', 'r').read()
    #sql_string = sql_string.replace("pcPart_id", str(pcPartId))
    #db = get_db()
    #cur = db.execute(sql_string, [pcPartId])
    #items = cur.fetchall()
    
    
""" ---------------- ---------------- List Items ---------------- ---------------- """
#Display Data - List All Items
@app.route('/item_list')
def item_list():
    sql_string = open('sql/select_all_items.sql', 'r').read()
    db = get_db()
    cur = db.execute(sql_string)
    items = cur.fetchall()
    return render_template('item_list.html', items=items)

#Display Form - Add Item
@app.route('/add_item')
def add_item():
    return render_template('add_item.html')
    
#Submit POST - Add Item
@app.route('/add', methods=['POST'])
def submit_item():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('insert into item (item_name, item_subtitle, \
                item_desc, item_category, item_condition, item_conditionDesc, item_cost) \
                values (?, ?, ?, ?, ?, ?, ?)',
                 [request.form['item_name'], 
                 request.form['item_subtitle'],
                 request.form['item_desc'],
                 request.form['item_category'],
                 request.form['item_condition'],
                 request.form['item_conditionDesc'],
                 request.form['item_cost']])
    db.commit()
    flash('New item was added to database!')
    return redirect(url_for('item_list'))





"""

"""

from clickhouse_driver import Client

client = Client(host='localhost',  # Use 'localhost' or '127.0.0.1' for a local server
                user='default',  # Default user, adjust if you've changed the user
                password='',  # Default installation has no password for 'default' user
                port=9000)  # Default TCP port for ClickHouse

# Attempt to execute a query
try:
    result = client.execute('SHOW TABLES')
    print(result)
except Exception as e:
    print(f"Encountered an error: {e}")

client.execute('SHOW TABLES')

client.execute('CREATE DATABASE IF NOT EXISTS town_cary')

client.execute('''
CREATE TABLE IF NOT EXISTS town_cary.crashes (
    id UInt64,
    location_description String,
    rdfeature String,
    rdsurface String,
    rdcondition String,
    lightcond String,
    weather String,
    crash_date Int64,
    year String,
    fatalities String,
    injuries String,
    month String
) ENGINE = MergeTree()
ORDER BY id
''')

import json

with open('crash-data.json', 'r') as file:
    data = json.load(file)

data = data['features']

# Вставка данных в таблицу
for feature in data:
    properties = feature['properties']

    # Определение crash_id
    crash_id = properties['tamainid']

    # Вставка данных о ДТП
    client.execute("""
    INSERT INTO town_cary.crashes (
        id, location_description, rdfeature,
        rdsurface, rdcondition, lightcond,
        weather, crash_date, year,
        fatalities, injuries, month
    ) VALUES""",
                   [(crash_id,
                     properties['location_description'] or "",
                     properties['rdfeature'] or "",
                     properties['rdsurface'] or "",
                     properties['rdcondition'] or "",
                     properties['lightcond'] or "",
                     properties['weather'] or "",
                     properties['crash_date'],
                     properties['year'],
                     properties['fatalities'] or "",
                     properties['injuries'] or "",
                     properties['month'])])

result = client.execute("SELECT * FROM town_cary.crashes")
print("Вставленная запись:", result[0])
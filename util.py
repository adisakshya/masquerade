import pandas as pd

def get_config_file_details(filename):

    filename = filename.split('_')
    connection_details = {}

    if len(filename) != 3:
        return connection_details

    ip_address = filename[2].split('.ovpn')[0]
    country = filename[1]
    
    try:
        df = pd.read_csv('./bin/connection_list.csv', index_col=0)
        row = df.loc[df['ip_address'] == ip_address]
        row = row.loc[row['country'] == country]
        row = row.fillna('Unknown')
        
        if len(row.index):
            connection_details = {
                'ip_address' : row['ip_address'][row.index[0]],
                'country' : row['country'][row.index[0]],
                'city' : row['city'][row.index[0]],
                'region' : row['region'][row.index[0]],
                'operator' : row['organisation'][row.index[0]]
            }

    except Exception as error:
        print("Error: ", error)
        pass
    
    return connection_details

def get_current_connection():
    
    current_connection_detail = {
        'country' : '',
        'ip_address' : '',
        'city' : '',
        'region' : '',
        'operator' : ''
    }

    data = []
    try:
        with open('./bin/current_connection.txt', "r") as f:
            data = f.read().split(',')
    except Exception as error:
        print("Error: ", error)
        return current_connection_detail
    
    if data:
        i = 0
        for key in current_connection_detail.keys():
            if data[i]:
                current_connection_detail[key] = data[i]
                i += 1
            else:
                current_connection_detail[key] = 'Unknown'
    else:
        return {}

    return current_connection_detail

def update_current_connection(update_config):
    
    try:
        if update_config:
            with open('./bin/current_connection.txt', "w") as f:
                line = update_config['country'] + ',' + update_config['ip_address'] + ',' + update_config['city'] + ',' + update_config['region'] + ',' + update_config['operator']
                f.write(line)
        else:
            return False
    except Exception as error:
        print("Error: ", error)
        return False
    
    return True

# print(get_config_file_details('vpngate_KR_12.4.56.78'))
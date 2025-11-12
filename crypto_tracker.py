#!/usr/bin/env python3
# Program for tracking crypto

import requests
import tkinter as tk
from datetime import datetime


def get_response(request_params):
    '''Get data from Coin Gecko'''
    base_url = 'https://api.coingecko.com/api/v3/'
    headers = {'x-cg-demo-api-key': request_params['api_key']}
    payload = {'vs_currencies': request_params['currency'], 'symbols': request_params['symbols']}
    path = 'simple/price'
    return requests.request('GET', base_url+path, headers=headers, params=payload).json()

def update_text(label, root, request_params, previous_vals):
    '''Main loop for updating text in window and making API calls'''
    update_time = 300000
    text = ""
    
    # Initialising all zeros for the first time around for the previous vals field.
    if previous_vals == None:
        response = {}
        for crypto in request_params['symbols'].split(','):
            response[crypto] = {request_params['currency']: 0}
            previous_vals = response
    try:
        # Test for HTTP failure, this section maybe done better
        # raise Exception
        response = get_response(request_params)
    except:
        text += f"!!!!Missed a http poll!!!\n\n"
    for coin, value in response.items():
        if (value['aud']) > previous_vals[coin]['aud']:
            indicator = chr(8593)
        elif (value['aud']) < previous_vals[coin]['aud']:
            indicator = chr(8595)
        else:
            indicator = '-'
        text += f'{coin.upper()}     $A {value['aud']}  {indicator}\n'
    
    text += f"\nUpdates every {update_time // 60000} minutes\nLast updated: {datetime.now().strftime('%H:%M:%S')}"
    label.config(text=text)
    root.after(update_time, lambda: update_text(label, root, request_params, response))  # Call again in 1 minute



def main():
    '''Main program'''
    with open('CONFIG', 'r') as config_file_handle:
        config_dict = {}
        for line in config_file_handle:
            split_line = line.rstrip('\n').split('=')
            if split_line[0] == 'api_key_file':
                api_key_file = split_line[1]
            elif split_line[0] == 'symbols':
                config_dict['symbols'] = split_line[1]
            elif split_line[0] == 'currency':
                config_dict['currency'] = split_line[1]
            else:
                raise Exception("Issue with content in CONFIG file")
            
    with open(api_key_file, 'r') as api_key_file:
        config_dict['api_key'] = api_key_file.readline().rstrip('\n')

    root = tk.Tk()
    root.title("Crypto Tracker")

    label = tk.Label(root, text="Initial text here", justify="left")
    label.pack(pady=20)

    update_text(label, root, config_dict, None)  # Start the updates
    root.mainloop()



if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
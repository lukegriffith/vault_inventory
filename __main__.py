import os
import hvac
import json

import inventory



'''
Inventory is ran from core AWX.
Team AWX read tenant inventories from host, includes SSH proxy.

'''


def main():
    '''
        main loads env vars
    '''


    client = hvac.Client(url=os.environ['VAULT_ADDR'], token=os.environ['VAULT_TOKEN'])
    kv = os.environ["vault_kv"]

    d = json.dumps(inventory.loadInventory(client, kv), default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)


    print(d)    



main()


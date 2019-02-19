import os 
import hvac
import inventory

class Tenant:
    def __init__(self, val, name):

        try:      
            self.name = val['name']
            self.ad_group = val['ad_group']
            self.owner = val['owner']
            self.svc_user = val['svc_user']
            self.svc_password = val['svc_password']
        
        except: 
            raise Exception("invalid tenant", name)



def loadInventory(client, kv):

    print("reading", kv)

    tenants = []

    for tenant in client.list(kv)['data']['keys']:

        raw = client.read(kv + '/' + tenant)['data']

        try:
            tenants.append(inventory.Tenant(raw, tenant))
        except:
            None
        
    return tenants

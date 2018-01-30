import requests
from ipaddr import IPNetwork, IPv4Network, IPv6Network


page = 'netixlan'
query = {'asn': 714}

netnod = [{'name':'sth-b',
           'mtu': 1500,
           'ipv4': 
           }]


def get_peeringdb_data(page, query):
  base_url = 'https://www.peeringdb.com/api'
  url = '/'.join([base_url, page])
  r = requests.get(url, params=query)
  if r.ok:
    return r.json().get('data')
  else:
      return {'error': 'Error! ' + str(r.status_code) + ' Tried: ' + r.url}


netnod_stockholm_ix_id = 70

ix = get_peeringdb_data('ix', {'id': netnod_stockholm_ix_id})
ixlans = get_peeringdb_data('ixlan', {'ix':70})

for ixlan in ixlans:
  ixlan_id = ixlan.get('id')
  ixpfxs = get_peeringdb_data('ixpfx', {'ixlan': ixlan_id})
  netixlan = get_peeringdb_data('netixlan', {'ixlan': ixlan_id})
  for ixpfx in ixpfxs:
    print ixlan_id
    print ixlan.get('name')
    print ixpfx.get('protocol')
    print ixpfx.get('prefix')












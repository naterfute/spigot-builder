import requests

def get_paper_versions():
  vapi='https://api.papermc.io/v2/projects/paper'
  vrequest=requests.get(vapi)
  vdata=vrequest.json()
  versions=vdata['versions']
  return versions

def get_vanilla_version():
  vapi='https://launchermeta.mojang.com/mc/game/version_manifest.json'
  vrequest=requests.get(vapi)
  vdata=vrequest.json()
  versions=vdata['versions']
  return versions



import requests
api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
linkedin_profile_url = 'https://www.linkedin.com/in/jorge-luis-olvera-olvera-7a203a2a9/'
api_key = 'dXvcL3RzsjiOHjwNaF35kA'
headers = {'Authorization': 'Bearer ' + api_key}

response = requests.get(api_endpoint,
                        params={'url': linkedin_profile_url,'skills': 'include'},
                        headers=headers)

print(response.json())

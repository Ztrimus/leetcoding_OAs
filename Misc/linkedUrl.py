from pprint import pprint
import requests


api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/company'

linkedin_profile_url = 'https://www.linkedin.com/company/gojektech/'

api_key = 'YOUR_API_KEY'

header_dic = {'Authorization': 'Bearer ' + api_key}



response = requests.get(api_endpoint,

                        *params*={'url': linkedin_profile_url},

                        *headers*=header_dic)

pprint(response.json())
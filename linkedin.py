from linkedin_api import Linkedin

# Authenticate using any Linkedin account credentials
api = Linkedin('holayosoygeorgi@gmail.com', 'Zorro117!')

# GET a profile
profile = api.get_profile('jorge-luis-olvera-olvera-7a203a2a9')

# GET a profiles contact info
contact_info = api.get_profile_contact_info('billy-g')

# GET 1st degree connections of a given profile
connections = api.get_profile_connections('1234asc12304')

print(profile)
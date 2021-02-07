from imgurpython import ImgurClient
import sys

# If you already have an access/refresh pair in hand
client_id = '40ce09cb894ea5d'
client_secret = '8b991489b7be222b4b991a7acee3d360b392ec81'
access_token = '35455cec21ebfa7f0f36b078a48526c69af3cbf2'
refresh_token = 'a0a7659f3ff8052be32a397eff3087dc9463fd69'

types = {"image/jpeg", "image/png"}

# Note since access tokens expire after an hour, only the refresh token is required (library handles autorefresh)
client = ImgurClient(client_id, client_secret, access_token, refresh_token)
album = client.gallery() #list

for item in album:
    try:
        if item.images[0]['type'] in types:
            print(item.images[0]['link'])
            print(item.images[0]['type'])
    except:
        print(sys.exc_info()[0])

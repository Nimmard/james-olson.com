import oauth2 as oauth

consumer_key = "190bb6da5eaaf0929c5f"
client_secret = "06c21931874e518df18d79375811d1b779b1729a"



consumer = oauth.consumer(key=consumer_key, secret=client_secret)

request_token_url = "https://github.com/login/oauth/access_token"

client = oauth.Client(consumer)
resp, content = client.request(request_token_url, "GET")
print resp
print content

import json
import tweepy

CONSUMER_KEY = 'qBbQVx7x5Z8qQGdvwVddGpYsh'
CONSUMER_SECRET = 'DKeUNiZGCoeDX7Lri8eNTmdEqSNMbu8wfaf700Y7NCNEqPRDZY'
OAUTH_TOKEN = '1675967766-vbbn8baYe0e4t2zYpGv1O5jxdVBgeqCgeo2g17L'
OAUTH_TOKEN_SECRET = 'j32CXSmvGVcP4VhVfl9JHwsOLRCOMIlvKjNRHznufRhmD'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)
count =900
res = tweepy.Cursor(api.search,
                    q="“bernie sanders",
                    since = "2019-04-06",
                    until = "2019-04-07",
                    result_type='mixed',
                    include_entities=True,
                    monitor_rate_limit=False,
                    wait_on_rate_limit=False,
                    tweet_mode= 'extended').items(100)
for i in res:
    print(count)
    with open('BS/data_'+str(count)+'.txt', 'w') as outfile:
        json.dump(i._json, outfile)
    count += 1
    print("=================")



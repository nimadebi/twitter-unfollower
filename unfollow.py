import tweepy

bearer = ""
access_token_key = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

client = tweepy.Client(bearer_token=bearer,
                       access_token=access_token_key,
                       access_token_secret=access_token_secret,
                       consumer_key=consumer_key,
                       consumer_secret=consumer_secret,
                       wait_on_rate_limit=True)

user = client.get_user(username="YOUR_USERNAME")
id = user[0].id

friends_request = client.get_users_following(id=id,max_results=1000)

for f in friends_request[0]:
    user = client.get_user(username=f)
    id = user[0].id
    client.unfollow_user(target_user_id=id)
    print("Unfollowed: " + str(f))

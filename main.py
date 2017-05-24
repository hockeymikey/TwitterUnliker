import twitter

api = twitter.Api(consumer_key='',
                  consumer_secret='',
                  access_token_key='',
                  access_token_secret='',
                  sleep_on_rate_limit=True)
print(api.VerifyCredentials())


# Get favorites for the current user.
while True:
    favorites = api.GetFavorites(count=200, include_entities=False)
    if len(favorites) <= 0:
        break
    print("Got list of {} favorites".format(len(favorites)))
    # Destroy each favorite.
    for status in favorites:
        try:
          api.DestroyFavorite(status=status)
          print("Destroying favorite on status {}".format(status.id))
        except Exception as ex:
          print(ex)
print("All done!")

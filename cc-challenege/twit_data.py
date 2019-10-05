import constants as CONSTANTS
import tweepy
import twitter
import requests
import json


# Authitcating API
auth = twitter.oauth.OAuth(CONSTANTS.ACCESS_KEY, CONSTANTS.ACCESS_SECRET, CONSTANTS.CONSUMER_KEY, CONSTANTS.CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

# The Yahoo! Where On Earth ID for the entire world is 1.
# See https://dev.twitter.com/docs/api/1.1/get/trends/place and
# http://developer.yahoo.com/geo/geoplanet/

WORLD_WOE_ID = 1
US_WOE_ID = 23424977

# Prefix ID with the underscore for query string parameterization.
# Without the underscore, the twitter package appends the ID value
# to the URL itself as a special case keyword argument.

world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
us_trends = twitter_api.trends.place(_id=US_WOE_ID)

def search_common_trends_in_the_world():
    world_trends_set = set([trend['name'] for trend in world_trends[0]['trends']])

    us_trends_set = set([trend['name'] for trend in us_trends[0]['trends']])

    common_trends = world_trends_set.intersection(us_trends_set)
    common_trends = [i.replace("#", "") for i in common_trends]

    return common_trends

def search_twitter_trends_by_place(trend_id):
    """
    Method to get the top 50 most current trends on twitter
    """
    trends = twitter_api.trends.place(_id=trend_id)

    # loop over the trends data and only get the hashtag value
    full_trend = [trend for trend in trends[0]['trends']]

    # get the hashtag only
    trends_list = []
    for i in full_trend:
        name = {}
        name['name'] = i['name'].replace('#', '')
        trends_list.append(name)

    return trends_list

# print(search_twitter_trends_by_place(1))

def search_get_location_with_trending_topics(trend_id):
    "Method to get the location of the trends"
    trends = twitter_api.trends.place(_id=trend_id)


def search_for_user(user_id):
    """
    Method to search for user based on passed in search criteria
    """
    user_data = twitter_api.users.search(q=f'{user_id}')

    # get the id_str, name, screen_name, location, and profile_image_url_https
    list_of_user_formatted_data = []

    for i in user_data:
        # create a new object to store the data
        user_data_obj = {}

        user_data_obj['id_str'] = i['id_str']
        user_data_obj['name'] = i['name']
        user_data_obj['screen_name'] = i['screen_name']
        user_data_obj['location'] = i['location']
        user_data_obj['profile_image_url'] = i['profile_image_url']
        list_of_user_formatted_data.append(user_data_obj)

    return list_of_user_formatted_data

post_data = search_twitter_trends_by_place(23424977)

def make_a_post_request(prepped_data):

    prepped_data = json.dumps(prepped_data)
    resp = requests.post(
        "http://localhost:4200/",
        data=json.dumps(prepped_data),
        headers={'Content-Type':'application/json'})

    # if resp.status_code != 201:
    #     print(f"response successfully: {resp.status_code}")
    # print('Created task. ID: {}'.format(resp.json()["id"]))

    return resp

# write to json file
def write_to_json_file(json_to_be_converted, json_file_name):
    with open(json_file_name, 'w') as json_file:
        json.dump(json_to_be_converted, json_file)

us_trends = search_twitter_trends_by_place(23424977)
location_based_on_trends = search_get_location_with_trending_topics(23424977)
user_info = search_for_user("Rob")


write_to_json_file(us_trends, 'us-trends.json')
write_to_json_file(user_info, 'user-ex.json')
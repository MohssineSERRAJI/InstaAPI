from defines import getCreds, makeApiCall
import sys
import json

def getHashtagInfo( params ) :
	""" Get info on a hashtag
	
	API Endpoint:
		https://graph.facebook.com/{graph-api-version}/ig_hashtag_search?user_id={user-id}&q={hashtag-name}&fields={fields}

	Returns:
		object: data from the endpoint

	"""

	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['user_id'] = params['instagram_account_id'] # user id making request
	endpointParams['q'] = params['hashtag_name'] # hashtag name
	endpointParams['fields'] = 'id,name' # fields to get back
	endpointParams['access_token'] = params['access_token'] # access token

	url = params['endpoint_base'] + 'ig_hashtag_search' # endpoint url

	return makeApiCall( url, endpointParams, params['debug'] ) # make the api call

def getHashtagMedia( params ) :
	""" Get posts for a hashtag
	
	API Endpoints:
		https://graph.facebook.com/{graph-api-version}/{ig-hashtag-id}/top_media?user_id={user-id}&fields={fields}
		https://graph.facebook.com/{graph-api-version}/{ig-hashtag-id}/recent_media?user_id={user-id}&fields={fields}

	Returns:
		object: data from the endpoint

	"""

	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['user_id'] = params['instagram_account_id'] # user id making request
	endpointParams['fields'] = 'id,caption,comment_count,like_count,media_type,media_url,permalink' # fields to get back
	endpointParams['access_token'] = params['access_token'] # access token

	url = params['endpoint_base'] + params['hashtag_id'] + '/' + params['type'] # endpoint url

	return makeApiCall( url, endpointParams, params['debug'] ) # make the api call

def getRecentlySearchedHashtags( params ) :
	""" Get hashtags a user has recently search for
	
	API Endpoints:
		https://graph.facebook.com/{graph-api-version}/{ig-user-id}/recently_searched_hashtags?fields={fields}

	Returns:
		object: data from the endpoint

	"""

	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['fields'] = 'id,name' # fields to get back
	endpointParams['access_token'] = params['access_token'] # access token

	url = params['endpoint_base'] + params['instagram_account_id'] + '/' + 'recently_searched_hashtags' # endpoint url

	return makeApiCall( url, endpointParams, params['debug'] ) # make the api call

try : # try and get param from command line
	hashtag = sys.argv[1] # hashtag to get info on
except : # default to coding hashtag
	hashtag = 'coding' # hashtag to get info on




def getHashtag_Media_by( hashtag , media_type) :
	'''
		Get posts for a hashtag.
		args:
			hashtag : the hashtag that you looking for  
			type : two values "top_media" or "recent_media"
	'''
	params = getCreds() # params for api call
	params['hashtag_name'] = hashtag # add on the hashtag we want to search for
	hashtagInfoResponse = getHashtagInfo( params ) # hit the api for some data!
	try:
		params['hashtag_id'] = hashtagInfoResponse['json_data']['data'][0]['id']; # store hashtag id
		params['type'] = media_type # set call to get top media for hashtag
	except:
		return None
	return getHashtagMedia( params )['json_data']['data'] # hit the api for some data!

# tvdb_api_v2.SearchApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_series_get**](SearchApi.md#search_series_get) | **GET** /search/series | 
[**search_series_params_get**](SearchApi.md#search_series_params_get) | **GET** /search/series/params | 


# **search_series_get**
> SeriesSearchResults search_series_get(name=name, imdb_id=imdb_id, zap2it_id=zap2it_id, slug=slug, accept_language=accept_language)



Allows the user to search for a series based on the following parameters.

### Example 
```python
from __future__ import print_function
import time
import tvdb_api_v2
from tvdb_api_v2.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwtToken
tvdb_api_v2.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# tvdb_api_v2.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = tvdb_api_v2.SearchApi()
name = 'name_example' # str | Name of the series to search for. (optional)
imdb_id = 'imdb_id_example' # str | IMDB id of the series (optional)
zap2it_id = 'zap2it_id_example' # str | Zap2it ID of the series to search for. (optional)
slug = 'slug_example' # str | Slug from site URL of series (https://www.thetvdb.com/series/$SLUG) (optional)
accept_language = 'accept_language_example' # str | Records are returned with the Episode name and Overview in the desired language, if it exists. If there is no translation for the given language, then the record is still returned but with empty values for the translated fields. (optional)

try: 
    api_response = api_instance.search_series_get(name=name, imdb_id=imdb_id, zap2it_id=zap2it_id, slug=slug, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_series_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the series to search for. | [optional] 
 **imdb_id** | **str**| IMDB id of the series | [optional] 
 **zap2it_id** | **str**| Zap2it ID of the series to search for. | [optional] 
 **slug** | **str**| Slug from site URL of series (https://www.thetvdb.com/series/$SLUG) | [optional] 
 **accept_language** | **str**| Records are returned with the Episode name and Overview in the desired language, if it exists. If there is no translation for the given language, then the record is still returned but with empty values for the translated fields. | [optional] 

### Return type

[**SeriesSearchResults**](SeriesSearchResults.md)

### Authorization

[jwtToken](../README.md#jwtToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_series_params_get**
> EpisodeDataQueryParams search_series_params_get()



Returns an array of parameters to query by in the `/search/series` route.

### Example 
```python
from __future__ import print_function
import time
import tvdb_api_v2
from tvdb_api_v2.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwtToken
tvdb_api_v2.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# tvdb_api_v2.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = tvdb_api_v2.SearchApi()

try: 
    api_response = api_instance.search_series_params_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_series_params_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EpisodeDataQueryParams**](EpisodeDataQueryParams.md)

### Authorization

[jwtToken](../README.md#jwtToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


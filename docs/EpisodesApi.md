# tvdb_api_v2.EpisodesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**episodes_id_get**](EpisodesApi.md#episodes_id_get) | **GET** /episodes/{id} | 


# **episodes_id_get**
> EpisodeRecordData episodes_id_get(id, accept_language=accept_language)



Returns the full information for a given episode id. __Deprecation Warning:__ The _director_ key will be deprecated in favor of the new _directors_ key in a future release.

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
api_instance = tvdb_api_v2.EpisodesApi()
id = 789 # int | ID of the episode
accept_language = 'accept_language_example' # str | Records are returned with the Episode name and Overview in the desired language, if it exists. If there is no translation for the given language, then the record is still returned but with empty values for the translated fields. (optional)

try: 
    api_response = api_instance.episodes_id_get(id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EpisodesApi->episodes_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the episode | 
 **accept_language** | **str**| Records are returned with the Episode name and Overview in the desired language, if it exists. If there is no translation for the given language, then the record is still returned but with empty values for the translated fields. | [optional] 

### Return type

[**EpisodeRecordData**](EpisodeRecordData.md)

### Authorization

[jwtToken](../README.md#jwtToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


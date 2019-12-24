# tvdb_api.MoviesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**movies_id_get**](MoviesApi.md#movies_id_get) | **GET** /movies/{id} | 
[**movieupdates_get**](MoviesApi.md#movieupdates_get) | **GET** /movieupdates | 


# **movies_id_get**
> Movie movies_id_get(id, accept_language=accept_language)



Returns a movies records that contains all information known about a particular movies id.

### Example
```python
from __future__ import print_function
import time
import tvdb_api
from tvdb_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwtToken
configuration = tvdb_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = tvdb_api.MoviesApi(tvdb_api.ApiClient(configuration))
id = 789 # int | ID of the movie
accept_language = 'accept_language_example' # str | Records are returned with the some fields in the desired language, if it exists. If there is no translation for the given language, then the record is still returned but with empty values for the translated fields. (optional)

try:
    api_response = api_instance.movies_id_get(id, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MoviesApi->movies_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the movie | 
 **accept_language** | **str**| Records are returned with the some fields in the desired language, if it exists. If there is no translation for the given language, then the record is still returned but with empty values for the translated fields. | [optional] 

### Return type

[**Movie**](Movie.md)

### Authorization

[jwtToken](../README.md#jwtToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **movieupdates_get**
> UpdatedMovies movieupdates_get(since)



Returns all movies ids updated since a given timestamp.

### Example
```python
from __future__ import print_function
import time
import tvdb_api
from tvdb_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwtToken
configuration = tvdb_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = tvdb_api.MoviesApi(tvdb_api.ApiClient(configuration))
since = 'since_example' # str | Epoch time to start your date range.

try:
    api_response = api_instance.movieupdates_get(since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MoviesApi->movieupdates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **str**| Epoch time to start your date range. | 

### Return type

[**UpdatedMovies**](UpdatedMovies.md)

### Authorization

[jwtToken](../README.md#jwtToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


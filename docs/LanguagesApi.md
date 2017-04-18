# tvdb_api_v2.LanguagesApi

All URIs are relative to *https://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**languages_get**](LanguagesApi.md#languages_get) | **GET** /languages | 
[**languages_id_get**](LanguagesApi.md#languages_id_get) | **GET** /languages/{id} | 


# **languages_get**
> LanguageData languages_get()



All available languages. These language abbreviations can be used in the `Accept-Language` header for routes that return translation records.

### Example 
```python
from __future__ import print_statement
import time
import tvdb_api_v2
from tvdb_api_v2.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwtToken
tvdb_api_v2.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# tvdb_api_v2.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = tvdb_api_v2.LanguagesApi()

try: 
    api_response = api_instance.languages_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguagesApi->languages_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LanguageData**](LanguageData.md)

### Authorization

[jwtToken](../README.md#jwtToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **languages_id_get**
> Language languages_id_get(id)



Information about a particular language, given the language ID.

### Example 
```python
from __future__ import print_statement
import time
import tvdb_api_v2
from tvdb_api_v2.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwtToken
tvdb_api_v2.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# tvdb_api_v2.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = tvdb_api_v2.LanguagesApi()
id = 'id_example' # str | ID of the language

try: 
    api_response = api_instance.languages_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguagesApi->languages_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the language | 

### Return type

[**Language**](Language.md)

### Authorization

[jwtToken](../README.md#jwtToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


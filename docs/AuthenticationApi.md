# tvdb_api_v2.AuthenticationApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login_post**](AuthenticationApi.md#login_post) | **POST** /login | 
[**refresh_token_get**](AuthenticationApi.md#refresh_token_get) | **GET** /refresh_token | 


# **login_post**
> Token login_post(authentication_string)



Returns a session token to be included in the rest of the requests. Note that API key authentication is required for all subsequent requests and user auth is required for routes in the `User` section

### Example 
```python
from __future__ import print_function
import time
import tvdb_api_v2
from tvdb_api_v2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = tvdb_api_v2.AuthenticationApi()
authentication_string = tvdb_api_v2.Auth() # Auth | JSON string containing your authentication details.

try: 
    api_response = api_instance.login_post(authentication_string)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->login_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authentication_string** | [**Auth**](Auth.md)| JSON string containing your authentication details. | 

### Return type

[**Token**](Token.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_token_get**
> Token refresh_token_get()



Refreshes your current, valid JWT token and returns a new token. Hit this route so that you do not have to post to `/login` with your API key and credentials once you have already been authenticated.

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
api_instance = tvdb_api_v2.AuthenticationApi()

try: 
    api_response = api_instance.refresh_token_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->refresh_token_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Token**](Token.md)

### Authorization

[jwtToken](../README.md#jwtToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


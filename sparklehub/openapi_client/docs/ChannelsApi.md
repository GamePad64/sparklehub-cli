# sparklehub.openapi_client.ChannelsApi

All URIs are relative to *http://127.0.0.1:8000/v1/sparkle*

Method | HTTP request | Description
------------- | ------------- | -------------
[**channels_list**](ChannelsApi.md#channels_list) | **GET** /channels/ | 
[**channels_read**](ChannelsApi.md#channels_read) | **GET** /channels/{id}/ | 


# **channels_list**
> list[Channel] channels_list()



### Example

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import sparklehub.openapi_client
from sparklehub.openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:8000/v1/sparkle
# See configuration.py for a list of all supported configuration parameters.
configuration = sparklehub.openapi_client.Configuration(
    host = "http://127.0.0.1:8000/v1/sparkle"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration = sparklehub.openapi_client.Configuration(
    host = "http://127.0.0.1:8000/v1/sparkle",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with sparklehub.openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sparklehub.openapi_client.ChannelsApi(api_client)
    
    try:
        api_response = api_instance.channels_list()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChannelsApi->channels_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Channel]**](Channel.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channels_read**
> Channel channels_read(id)



### Example

* Api Key Authentication (Token):
```python
from __future__ import print_function
import time
import sparklehub.openapi_client
from sparklehub.openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:8000/v1/sparkle
# See configuration.py for a list of all supported configuration parameters.
configuration = sparklehub.openapi_client.Configuration(
    host = "http://127.0.0.1:8000/v1/sparkle"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration = sparklehub.openapi_client.Configuration(
    host = "http://127.0.0.1:8000/v1/sparkle",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with sparklehub.openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sparklehub.openapi_client.ChannelsApi(api_client)
    id = 'id_example' # str | A UUID string identifying this channel.

    try:
        api_response = api_instance.channels_read(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChannelsApi->channels_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this channel. | 

### Return type

[**Channel**](Channel.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


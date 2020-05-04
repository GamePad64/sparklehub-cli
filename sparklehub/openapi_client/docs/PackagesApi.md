# sparklehub.openapi_client.PackagesApi

All URIs are relative to *http://127.0.0.1:8000/v1/sparkle*

Method | HTTP request | Description
------------- | ------------- | -------------
[**packages_create**](PackagesApi.md#packages_create) | **POST** /packages/ | 
[**packages_delete**](PackagesApi.md#packages_delete) | **DELETE** /packages/{id}/ | 
[**packages_list**](PackagesApi.md#packages_list) | **GET** /packages/ | 
[**packages_partial_update**](PackagesApi.md#packages_partial_update) | **PATCH** /packages/{id}/ | 
[**packages_read**](PackagesApi.md#packages_read) | **GET** /packages/{id}/ | 
[**packages_update**](PackagesApi.md#packages_update) | **PUT** /packages/{id}/ | 


# **packages_create**
> Package packages_create(data)



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
    api_instance = sparklehub.openapi_client.PackagesApi(api_client)
    data = sparklehub.openapi_client.Package() # Package | 

    try:
        api_response = api_instance.packages_create(data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PackagesApi->packages_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Package**](Package.md)|  | 

### Return type

[**Package**](Package.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **packages_delete**
> packages_delete(id)



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
    api_instance = sparklehub.openapi_client.PackagesApi(api_client)
    id = 'id_example' # str | A UUID string identifying this package.

    try:
        api_instance.packages_delete(id)
    except ApiException as e:
        print("Exception when calling PackagesApi->packages_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this package. | 

### Return type

void (empty response body)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **packages_list**
> list[Package] packages_list(release=release, slug=slug)



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
    api_instance = sparklehub.openapi_client.PackagesApi(api_client)
    release = 'release_example' # str |  (optional)
slug = 'slug_example' # str |  (optional)

    try:
        api_response = api_instance.packages_list(release=release, slug=slug)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PackagesApi->packages_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release** | **str**|  | [optional] 
 **slug** | **str**|  | [optional] 

### Return type

[**list[Package]**](Package.md)

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

# **packages_partial_update**
> Package packages_partial_update(id, data)



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
    api_instance = sparklehub.openapi_client.PackagesApi(api_client)
    id = 'id_example' # str | A UUID string identifying this package.
data = sparklehub.openapi_client.Package() # Package | 

    try:
        api_response = api_instance.packages_partial_update(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PackagesApi->packages_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this package. | 
 **data** | [**Package**](Package.md)|  | 

### Return type

[**Package**](Package.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **packages_read**
> Package packages_read(id)



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
    api_instance = sparklehub.openapi_client.PackagesApi(api_client)
    id = 'id_example' # str | A UUID string identifying this package.

    try:
        api_response = api_instance.packages_read(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PackagesApi->packages_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this package. | 

### Return type

[**Package**](Package.md)

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

# **packages_update**
> Package packages_update(id, data)



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
    api_instance = sparklehub.openapi_client.PackagesApi(api_client)
    id = 'id_example' # str | A UUID string identifying this package.
data = sparklehub.openapi_client.Package() # Package | 

    try:
        api_response = api_instance.packages_update(id, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PackagesApi->packages_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this package. | 
 **data** | [**Package**](Package.md)|  | 

### Return type

[**Package**](Package.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


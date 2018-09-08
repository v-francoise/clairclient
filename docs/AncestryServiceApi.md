# clairclient.AncestryServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ancestry**](AncestryServiceApi.md#get_ancestry) | **GET** /ancestry/{ancestry_name} | 
[**post_ancestry**](AncestryServiceApi.md#post_ancestry) | **POST** /ancestry | 


# **get_ancestry**
> ClairpbGetAncestryResponse get_ancestry(ancestry_name, with_vulnerabilities=with_vulnerabilities, with_features=with_features)



### Example
```python
from __future__ import print_function
import time
import clairclient
from clairclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clairclient.AncestryServiceApi()
ancestry_name = 'ancestry_name_example' # str | 
with_vulnerabilities = True # bool |  (optional)
with_features = True # bool |  (optional)

try:
    api_response = api_instance.get_ancestry(ancestry_name, with_vulnerabilities=with_vulnerabilities, with_features=with_features)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AncestryServiceApi->get_ancestry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ancestry_name** | **str**|  | 
 **with_vulnerabilities** | **bool**|  | [optional] 
 **with_features** | **bool**|  | [optional] 

### Return type

[**ClairpbGetAncestryResponse**](ClairpbGetAncestryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_ancestry**
> ClairpbPostAncestryResponse post_ancestry(clairpb_post_ancestry_request)



### Example
```python
from __future__ import print_function
import time
import clairclient
from clairclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clairclient.AncestryServiceApi()
clairpb_post_ancestry_request = clairclient.ClairpbPostAncestryRequest() # ClairpbPostAncestryRequest | 

try:
    api_response = api_instance.post_ancestry(clairpb_post_ancestry_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AncestryServiceApi->post_ancestry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clairpb_post_ancestry_request** | [**ClairpbPostAncestryRequest**](ClairpbPostAncestryRequest.md)|  | 

### Return type

[**ClairpbPostAncestryResponse**](ClairpbPostAncestryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


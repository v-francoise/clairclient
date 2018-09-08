# clairclient.NotificationServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_notification**](NotificationServiceApi.md#get_notification) | **GET** /notifications/{name} | 
[**mark_notification_as_read**](NotificationServiceApi.md#mark_notification_as_read) | **DELETE** /notifications/{name} | 


# **get_notification**
> ClairpbGetNotificationResponse get_notification(name, old_vulnerability_page=old_vulnerability_page, new_vulnerability_page=new_vulnerability_page, limit=limit)



### Example
```python
from __future__ import print_function
import time
import clairclient
from clairclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clairclient.NotificationServiceApi()
name = 'name_example' # str | 
old_vulnerability_page = 'old_vulnerability_page_example' # str | if the vulnerability_page is empty, it implies the first page. (optional)
new_vulnerability_page = 'new_vulnerability_page_example' # str |  (optional)
limit = 56 # int |  (optional)

try:
    api_response = api_instance.get_notification(name, old_vulnerability_page=old_vulnerability_page, new_vulnerability_page=new_vulnerability_page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationServiceApi->get_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **old_vulnerability_page** | **str**| if the vulnerability_page is empty, it implies the first page. | [optional] 
 **new_vulnerability_page** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**ClairpbGetNotificationResponse**](ClairpbGetNotificationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_notification_as_read**
> ProtobufEmpty mark_notification_as_read(name)



### Example
```python
from __future__ import print_function
import time
import clairclient
from clairclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clairclient.NotificationServiceApi()
name = 'name_example' # str | 

try:
    api_response = api_instance.mark_notification_as_read(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationServiceApi->mark_notification_as_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**ProtobufEmpty**](ProtobufEmpty.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# clairclient
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 3.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import clairclient 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import clairclient
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import clairclient
from clairclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = clairclient.AncestryServiceApi(clairclient.ApiClient(configuration))
ancestry_name = 'ancestry_name_example' # str | 
with_vulnerabilities = True # bool |  (optional)
with_features = True # bool |  (optional)

try:
    api_response = api_instance.get_ancestry(ancestry_name, with_vulnerabilities=with_vulnerabilities, with_features=with_features)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AncestryServiceApi->get_ancestry: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AncestryServiceApi* | [**get_ancestry**](docs/AncestryServiceApi.md#get_ancestry) | **GET** /ancestry/{ancestry_name} | 
*AncestryServiceApi* | [**post_ancestry**](docs/AncestryServiceApi.md#post_ancestry) | **POST** /ancestry | 
*NotificationServiceApi* | [**get_notification**](docs/NotificationServiceApi.md#get_notification) | **GET** /notifications/{name} | 
*NotificationServiceApi* | [**mark_notification_as_read**](docs/NotificationServiceApi.md#mark_notification_as_read) | **DELETE** /notifications/{name} | 


## Documentation For Models

 - [ClairpbAncestry](docs/ClairpbAncestry.md)
 - [ClairpbClairStatus](docs/ClairpbClairStatus.md)
 - [ClairpbFeature](docs/ClairpbFeature.md)
 - [ClairpbGetAncestryResponse](docs/ClairpbGetAncestryResponse.md)
 - [ClairpbGetNotificationResponse](docs/ClairpbGetNotificationResponse.md)
 - [ClairpbIndexedAncestryName](docs/ClairpbIndexedAncestryName.md)
 - [ClairpbLayer](docs/ClairpbLayer.md)
 - [ClairpbNotification](docs/ClairpbNotification.md)
 - [ClairpbPagedVulnerableAncestries](docs/ClairpbPagedVulnerableAncestries.md)
 - [ClairpbPostAncestryRequest](docs/ClairpbPostAncestryRequest.md)
 - [ClairpbPostAncestryResponse](docs/ClairpbPostAncestryResponse.md)
 - [ClairpbVulnerability](docs/ClairpbVulnerability.md)
 - [PostAncestryRequestPostLayer](docs/PostAncestryRequestPostLayer.md)
 - [ProtobufEmpty](docs/ProtobufEmpty.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author





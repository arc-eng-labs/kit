# pr_pilot.TaskRetrievalApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tasks_retrieve**](TaskRetrievalApi.md#tasks_retrieve) | **GET** /api/tasks/{id}/ | 


# **tasks_retrieve**
> Task tasks_retrieve(id)



### Example

* Api Key Authentication (apiKeyAuth):

```python
import pr_pilot
from pr_pilot.models.task import Task
from pr_pilot.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = pr_pilot.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pr_pilot.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pr_pilot.TaskRetrievalApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.tasks_retrieve(id)
        print("The response of TaskRetrievalApi->tasks_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskRetrievalApi->tasks_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Task**](Task.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | The specified task does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

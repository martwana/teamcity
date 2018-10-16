# coding: utf-8

"""
    TeamCity REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 10.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from dohq_teamcity.api_client import ApiClient


class ProblemOccurrenceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_problems(self, **kwargs):  # noqa: E501
        """get_problems  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_problems(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str locator:
        :param str fields:
        :return: ProblemOccurrences
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_problems_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_problems_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_problems_with_http_info(self, **kwargs):  # noqa: E501
        """get_problems  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_problems_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str locator:
        :param str fields:
        :return: ProblemOccurrences
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['locator', 'fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_problems" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'locator' in params:
            query_params.append(('locator', params['locator']))  # noqa: E501
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/app/rest/problemOccurrences', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProblemOccurrences',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def serve_instance(self, problem_locator, **kwargs):  # noqa: E501
        """serve_instance  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.serve_instance(problem_locator, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str problem_locator: (required)
        :param str fields:
        :return: ProblemOccurrence
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.serve_instance_with_http_info(problem_locator, **kwargs)  # noqa: E501
        else:
            (data) = self.serve_instance_with_http_info(problem_locator, **kwargs)  # noqa: E501
            return data

    def serve_instance_with_http_info(self, problem_locator, **kwargs):  # noqa: E501
        """serve_instance  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.serve_instance_with_http_info(problem_locator, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str problem_locator: (required)
        :param str fields:
        :return: ProblemOccurrence
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['problem_locator', 'fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method serve_instance" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'problem_locator' is set
        if ('problem_locator' not in params or
                params['problem_locator'] is None):
            raise ValueError("Missing the required parameter `problem_locator` when calling `serve_instance`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'problem_locator' in params:
            path_params['problemLocator'] = params['problem_locator']  # noqa: E501

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/app/rest/problemOccurrences/{problemLocator}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProblemOccurrence',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

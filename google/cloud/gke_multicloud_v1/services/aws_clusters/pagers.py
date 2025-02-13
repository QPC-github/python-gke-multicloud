# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from typing import (
    Any,
    AsyncIterator,
    Awaitable,
    Callable,
    Iterator,
    Optional,
    Sequence,
    Tuple,
)

from google.cloud.gke_multicloud_v1.types import aws_resources, aws_service


class ListAwsClustersPager:
    """A pager for iterating through ``list_aws_clusters`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gke_multicloud_v1.types.ListAwsClustersResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``aws_clusters`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAwsClusters`` requests and continue to iterate
    through the ``aws_clusters`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gke_multicloud_v1.types.ListAwsClustersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., aws_service.ListAwsClustersResponse],
        request: aws_service.ListAwsClustersRequest,
        response: aws_service.ListAwsClustersResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gke_multicloud_v1.types.ListAwsClustersRequest):
                The initial request object.
            response (google.cloud.gke_multicloud_v1.types.ListAwsClustersResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = aws_service.ListAwsClustersRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[aws_service.ListAwsClustersResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[aws_resources.AwsCluster]:
        for page in self.pages:
            yield from page.aws_clusters

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAwsClustersAsyncPager:
    """A pager for iterating through ``list_aws_clusters`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gke_multicloud_v1.types.ListAwsClustersResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``aws_clusters`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAwsClusters`` requests and continue to iterate
    through the ``aws_clusters`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gke_multicloud_v1.types.ListAwsClustersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[aws_service.ListAwsClustersResponse]],
        request: aws_service.ListAwsClustersRequest,
        response: aws_service.ListAwsClustersResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gke_multicloud_v1.types.ListAwsClustersRequest):
                The initial request object.
            response (google.cloud.gke_multicloud_v1.types.ListAwsClustersResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = aws_service.ListAwsClustersRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[aws_service.ListAwsClustersResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[aws_resources.AwsCluster]:
        async def async_generator():
            async for page in self.pages:
                for response in page.aws_clusters:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAwsNodePoolsPager:
    """A pager for iterating through ``list_aws_node_pools`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gke_multicloud_v1.types.ListAwsNodePoolsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``aws_node_pools`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAwsNodePools`` requests and continue to iterate
    through the ``aws_node_pools`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gke_multicloud_v1.types.ListAwsNodePoolsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., aws_service.ListAwsNodePoolsResponse],
        request: aws_service.ListAwsNodePoolsRequest,
        response: aws_service.ListAwsNodePoolsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gke_multicloud_v1.types.ListAwsNodePoolsRequest):
                The initial request object.
            response (google.cloud.gke_multicloud_v1.types.ListAwsNodePoolsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = aws_service.ListAwsNodePoolsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[aws_service.ListAwsNodePoolsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[aws_resources.AwsNodePool]:
        for page in self.pages:
            yield from page.aws_node_pools

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAwsNodePoolsAsyncPager:
    """A pager for iterating through ``list_aws_node_pools`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.gke_multicloud_v1.types.ListAwsNodePoolsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``aws_node_pools`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAwsNodePools`` requests and continue to iterate
    through the ``aws_node_pools`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.gke_multicloud_v1.types.ListAwsNodePoolsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[aws_service.ListAwsNodePoolsResponse]],
        request: aws_service.ListAwsNodePoolsRequest,
        response: aws_service.ListAwsNodePoolsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.gke_multicloud_v1.types.ListAwsNodePoolsRequest):
                The initial request object.
            response (google.cloud.gke_multicloud_v1.types.ListAwsNodePoolsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = aws_service.ListAwsNodePoolsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[aws_service.ListAwsNodePoolsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[aws_resources.AwsNodePool]:
        async def async_generator():
            async for page in self.pages:
                for response in page.aws_node_pools:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)

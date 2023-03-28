import pytest
import requests_mock
from mcs.common import constants as c

from mcs import APIClient, BucketAPI
from dotenv import load_dotenv
import os

from mcs.object.bucket_storage import Bucket

load_dotenv('.env_test')
api_key = os.getenv('api_key')
access_token = os.getenv('access_token')
chain_name = os.getenv('chain_name')
wrong_chain_name = os.getenv('wrong_chain_name')
wrong_api_key = os.getenv('wrong_api_key')
wrong_access_token = os.getenv('wrong_access_token')


@pytest.fixture()
def shared_mock_bucket(shared_mock_api_client):
    with requests_mock.Mocker() as m:
        m.get(c.GET_GATEWAY, json={'status': 'success', 'data': 'https://8e88328c1.acl.multichain.storage'})
        bucket_api = BucketAPI(shared_mock_api_client)
        return bucket_api


@pytest.fixture()
def shared_mock_api_client():
    with requests_mock.Mocker() as m:
        m.register_uri(c.POST, c.APIKEY_LOGIN, json={"data": {"jwt_token": "sample_token"}})
        api_client = APIClient(api_key="sample_api_key", access_token="sample_access_token",
                               chain_name="polygon.mumbai")
        return api_client


@pytest.fixture()
def shared_real_bucket():
    bucket = BucketAPI(APIClient(api_key, access_token, chain_name))
    return bucket


@pytest.fixture()
def shared_real_api_client():
    api_client = APIClient(api_key, access_token, chain_name)
    return api_client


@pytest.fixture()
def shared_login_info():
    return {
        "api_key": api_key,
        "access_token": access_token,
        "chain_name": chain_name,
        "wrong_chain_name": wrong_chain_name,
        "wrong_api_key": wrong_api_key,
        "wrong_access_token": wrong_access_token
    }


@pytest.fixture()
def shared_bucket_list():
    bucket_info = [{
        'bucket_name': 'test-bucket-1',
        'deleted_at': None,
        'bucket_uid': 'bucket_uid',
        'address': '0x5339595102d92a',
        'max_size': 34359738368,
        'size': 254,
        'is_free': True,
        'payment_tx': '',
        'is_active': True,
        'is_deleted': False,
        'file_number': 2,
        'id': 19,
        'created_at': '2023-01-05T19:00:01Z',
        'updated_at': '2023-01-05T19:00:01Z',
    },
        {
            'bucket_name': 'test-bucket-2',
            'deleted_at': None,
            'bucket_uid': 'db069404-f846-3wasdf',
            'address': '0x5asdfsadfadsfaewf2d92a',
            'max_size': 34359738368,
            'size': 2524,
            'is_free': True,
            'payment_tx': '',
            'is_active': True,
            'is_deleted': False,
            'file_number': 22,
            'id': 191233,
            'created_at': '2023-01-05T19:00:01Z',
            'updated_at': '2023-01-05T19:00:01Z', }]
    return bucket_info
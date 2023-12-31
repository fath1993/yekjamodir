import json
import threading

import requests

from yekjamodir.settings import ARVAN_CLOUD_API_KEY


def create_cname(blog, domain_key):
    url = 'https://napi.arvancloud.ir/cdn/4.0/domains/yekjamodir.ir/dns-records'

    headers = {
        'authority': 'napi.arvancloud.ir',
        'accept': 'application/json, text/plain, */*',
        'authorization': f'Apikey {ARVAN_CLOUD_API_KEY}',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
    }

    data = {
        "value":
            {
                "host": f"yekjamodir.ir",
                "host_header": "source",
                "port": 1
            },
            "type": "cname",
            "name": f"{domain_key}",
            "ttl": 120,
            "cloud": False,
            "upstream_https": "default",
            "ip_filter_mode":
                {
                    "count": "single",
                    "order": "none",
                    "geo_filter": "none"
                }
    }
    blog.generated_url_id = 'در حال تایید'
    try:
        response = requests.post(url=url, headers=headers, json=data)
        print(response.text)
        try:
            blog.generated_url_id = json.loads(response.text)['data']['id']
        except:
            blog.generated_url_id = 'عدم تایید'
    except Exception as e:
        response = str(e)
        blog.generated_url_id = 'عدم تایید'
        print(response)
    blog.save()


class CreateCnameThread(threading.Thread):
    def __init__(self, blog, domain_key):
        super().__init__()
        self.domain_key = domain_key
        self.blog = blog

    def run(self):
        create_cname(self.blog, self.domain_key)
        return


def delete_cname(cname_id):
    url = f'https://napi.arvancloud.ir/cdn/4.0/domains/yekjamodir.ir/dns-records/{cname_id}'
    try:
        response = requests.delete(url)
    except Exception as e:
        response = str(e)
    print(response.text)
    return response


class DeleteCnameThread(threading.Thread):
    def __init__(self, cname_id):
        super().__init__()
        self.cname_id = cname_id

    def run(self):
        delete_cname(self.cname_id)
        return
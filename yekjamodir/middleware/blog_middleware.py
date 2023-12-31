from urllib.parse import urlparse

from django.contrib.sites.models import Site
from django.shortcuts import render


class BlogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        panel_domain = Site.objects.get_current().domain
        panel_domain_host = str(panel_domain).replace('https://', '').replace('http://', '').replace('/', ' ').split()[
            0]
        # print(site_domain_host)
        requested_url = urlparse(request.build_absolute_uri())
        requested_url_scheme = requested_url.scheme  # Extract scheme (http/https)
        requested_url_host = requested_url.netloc  # Extract host (including port if present)
        requested_url_path = requested_url.path  # Extract path

        allowed_path_list = ['/', '/blog-front-post-list/', '/blog-front-contact-us/',
                             '/blog-front-about-us/']
        request.x_blog = False
        request.x_blog_subdomain = False
        if requested_url_host != '127.0.0.1:8000':  # make sure we are not at dev situation
            if requested_url_host != panel_domain_host:  # means it is blog
                request.x_blog = True
                if str(requested_url_host).find(f'.{panel_domain_host}') != -1:
                    request.x_blog_subdomain = True
                else:
                    request.x_blog_subdomain = False
                if not requested_url_path in allowed_path_list:
                    if requested_url_path.find('blog-front-post-detail&id') != -1:
                        pass
                    else:
                        return render(request, 'blog-theme-1/new-design/img/.html')
        return self.get_response(request)

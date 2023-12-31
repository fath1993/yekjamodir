import threading

from blog.models import BlogPostUserView
import socket


class BlogPostViewCounterThread(threading.Thread):
    def __init__(self, post, published_on):
        super().__init__()
        self.post = post
        self.published_on = published_on

    def run(self):
        try:
            hostname = socket.gethostname()
            ip_address = socket.gethostbyname(hostname)
            if self.published_on == 'panel':
                view_on_main_panel = True
                view_on_namaye_javani = False
            else:
                view_on_main_panel = False
                view_on_namaye_javani = True

            try:
                created_blog_post_view_count = BlogPostUserView.objects.get(user_host_name=hostname,
                                                                            user_ip_address=ip_address,
                                                                            blog_post=self.post)
                if view_on_main_panel:
                    created_blog_post_view_count.view_on_main_panel = True
                    created_blog_post_view_count.save()
                if view_on_namaye_javani:
                    created_blog_post_view_count.view_on_namaye_javani = True
                    created_blog_post_view_count.save()
            except:
                new_blog_post_view_count = BlogPostUserView.objects.create(user_host_name=hostname,
                                                                           user_ip_address=ip_address,
                                                                           blog_post=self.post)
                if view_on_main_panel:
                    new_blog_post_view_count.view_on_main_panel = True
                    new_blog_post_view_count.save()
                if view_on_namaye_javani:
                    new_blog_post_view_count.view_on_namaye_javani = True
                    new_blog_post_view_count.save()
        except:
            pass
        return

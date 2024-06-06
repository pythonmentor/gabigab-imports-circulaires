from django.db import models


class Comment(models.Model):
    blog_page = models.ForeignKey("blog.BlogPage", on_delete=models.CASCADE)
    email = models.EmailField()
    content = models.TextField()

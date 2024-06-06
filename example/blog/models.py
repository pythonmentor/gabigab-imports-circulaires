from django.db import models
from django.shortcuts import render

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel

from example.comments.forms import CommentForm


class BlogPage(Page):
    date = models.DateField(verbose_name="Date de publication")
    intro = RichTextField()
    body = StreamField(
        [],
        use_json_field=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("date"),
        FieldPanel("intro"),
        FieldPanel("body"),
    ]

    def serve(self, request, *args, **kwargs):
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                ...  # faire quelque chose d'intelligent
                return render(
                    request,
                    "blog/thankyou.html",
                    context={"page": self, "form": form, "success": True},
                )
        form = CommentForm()
        return render(
            request,
            "blog/blog_page.html",
            context={"page": self, "form": form},
        )

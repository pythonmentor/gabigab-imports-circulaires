# Generated by Django 5.0.6 on 2024-06-06 09:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("comments", "0003_alter_comment_blog_page"),
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="BlogPage",
        ),
    ]
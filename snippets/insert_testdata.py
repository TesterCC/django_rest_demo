# coding=utf-8

# run in python manage.py shell
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# 创建数据
snippet = Snippet(code='foo2 = "bar"\n')
snippet.save()

snippet = Snippet(code='print2 "hello, world"\n')
snippet.save()
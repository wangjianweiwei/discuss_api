# -*- coding: utf-8 -*-
"""
@Author：wang jian wei
@date：2023/5/5 21:54
"""
from django.db import models


class FlexibleForeignKey(models.ForeignKey):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("on_delete", models.CASCADE)
        super().__init__(*args, **kwargs)

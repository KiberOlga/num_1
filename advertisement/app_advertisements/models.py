# -*- coding: cp1251 -*-
from django.db import models


class Advertisement(models.Model):
    title = models.CharField("���������", max_length=128)
    description = models.TextField("��������")
    price = models.DecimalField("����", max_digits=10, decimal_places=2)
    auction = models.BooleanField("����", help_text="��������, ���� ���� �������")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'advertisements'

    def __str__(self):
        obj = 'Advertisement(id={0.id}, title={0.title}, price={0.price})'
        return obj.format(self)













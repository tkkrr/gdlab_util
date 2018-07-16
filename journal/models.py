from datetime import datetime, timedelta

from django.db import models
from django.utils import timezone


class Journal(models.Model):
    weekdays = []
    now = timezone.now()
    today_week = now.weekday()
    if today_week < 2:
        today_week = today_week+6
    #水曜日基準に変更。
    today_week = today_week - 2
    #各日付(date型)を配列に格納
    for day in range(0,7):
        tmp_week = day - today_week
        tmp_day = now + timedelta(days=tmp_week)
        weekdays.append(tmp_day)
    name    = models.CharField('氏名', max_length=30, null=False)
    date    = models.DateField('作成日', default=now, null=False)
    wens    = models.CharField(str(weekdays[0].month)+'/'+str(weekdays[0].day)+'(水)', max_length=100, default='なし')
    thurs   = models.CharField(str(weekdays[1].month)+'/'+str(weekdays[1].day)+'(木)', max_length=100, default='なし')
    fri     = models.CharField(str(weekdays[2].month)+'/'+str(weekdays[2].day)+'(金)', max_length=100, default='なし')
    satur   = models.CharField(str(weekdays[3].month)+'/'+str(weekdays[3].day)+'(土)', max_length=100, default='なし')
    sun     = models.CharField(str(weekdays[4].month)+'/'+str(weekdays[4].day)+'(日)', max_length=100, default='なし')
    mon     = models.CharField(str(weekdays[5].month)+'/'+str(weekdays[5].day)+'(月)', max_length=100, default='なし')
    tues    = models.CharField(str(weekdays[6].month)+'/'+str(weekdays[6].day)+'(火)', max_length=100, default='なし')
    journal = models.TextField('所感,次週への感想', default="特になし。")

    def __str__(self):
        # title = self.name + "," + self.date + "," + self.journal
        return self.name

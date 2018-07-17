from django.shortcuts import render, get_object_or_404

from django.views import View, generic
from django.http import HttpResponse
from django.utils import timezone
from datetime import datetime, timedelta
from socket import gethostname

from .forms import JournalForm
from .models import Journal

import pdfkit

class IndexView(generic.ListView):
    model = Journal
    template_name = 'journal/index.html'


class CreateView(generic.CreateView):
    model = Journal
    form_class = JournalForm
    template_name = "journal/form.html"
    success_url = "/journal"  # 成功時にリダイレクトするURL


class UpdateView(generic.UpdateView):
    model = Journal
    form_class = JournalForm
    template_name = 'journal/update.html'
    success_url = "/"


# class PdfView():
#     model = Journal
#     template_name = 'journal/pdfview.html'
#     success_url = "/journal"

def pdfview(request, journal_id):
    journal = Journal.objects.get(id=journal_id)
    # print(journal)
    # pdf用のContent-TypeやContent-Dispositionをセット
    response = HttpResponse(_create_pdf(journal), content_type='application/pdf', status=200)
    response['Content-Disposition'] = 'filename="example.pdf"'
    # 即ダウンロードしたい時は、attachmentをつける
    # response['Content-Disposition'] = 'attachment; filename="example.pdf"'
    return response


def _create_pdf(content):
        if 'takakurarei-no-MacBook-Pro.local' in gethostname():
            config = pdfkit.configuration(wkhtmltopdf="/usr/local/bin/wkhtmltopdf")
        else:
            config = pdfkit.configuration(wkhtmltopdf="/app/bin/wkhtmltopdf")

        options = {
            'page-size': 'A4',
            'margin-top': '0.5in',
            'margin-right': '0.5in',
            'margin-bottom': '0.5in',
            'margin-left': '0.5in',
            'encoding': "UTF-8",
            'no-outline': None,
            'dpi': '72'
        }

        html = '''
        <html lang="ja"><meta charset="utf-8">
        <body>
        <div class="container">
            <header class="under-line">
                <span class="headding">週間ジャーナル</span>
                <span class="right light">'''
        html += '作成日：' + str(content.date.year) +'年 ' + str(content.date.month)+'月 ' + str(content.date.day)  +'日'  + '<br/>作成者：' + content.name
        html += '''
        </span></header>
        <style>
        html,body{
            height:297mm;
            width:210mm;
            font-family: 'ヒラギノ角ゴシック','Hiragino Sans','メイリオ', Meiryo,'Arial Rounded MT Bold',sans-serif;
        }
        .container{
          height: 297mm;
          width: 210mm;
          border: solid 1px #ccc;
        }
        .under-line{
          width:190mm;
          border-bottom: solid 5px #cc3;
          border-radius: 2px;
          margin-top: 30px;
          margin-left: 20px;
          padding-left: 30px;
          padding-bottom: 5px;
        }
        .headding{
          font-weight: 600;
          font-size: 2em;
          width: 80%;
        }
        .right{
          margin-top: 8px;
          margin-right: 20px;
          float: right;
          line-height: 18px;
          text-align: right;
        }
        .li-left{
          width:30mm;
          float: left;
        }
        .light{
          font-weight: lighter;
        }
        h1{
          margin-left: 15px;
          margin-top: 40px;
        }
        li{
          font-weight: bold;
          list-style: none;
          padding: 10px 0px 10px 10px;
          margin-right: 30px;
          display: flex;
          border-bottom: solid 1px #ddd;
          align-items: center;
        }
        li:nth-child(even){
          background: #eee;
        }
        p{
          margin-left: 45px;
          margin-right: 30px;
        }
        </style>
        <main>
        <h1>・ジャーナル</h1><ul>
        '''
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

        html += '<li><div class="li-left">' + str(weekdays[0].month)+'/'+str(weekdays[0].day)+'(水)</div><div>' + content.wens  + '</div></li>'
        html += '<li><div class="li-left">' + str(weekdays[1].month)+'/'+str(weekdays[1].day)+'(木)</div><div>' + content.thurs + '</div></li>'
        html += '<li><div class="li-left">' + str(weekdays[2].month)+'/'+str(weekdays[2].day)+'(金)</div><div>' + content.fri   + '</div></li>'
        html += '<li><div class="li-left">' + str(weekdays[3].month)+'/'+str(weekdays[3].day)+'(土)</div><div>' + content.satur + '</div></li>'
        html += '<li><div class="li-left">' + str(weekdays[4].month)+'/'+str(weekdays[4].day)+'(日)</div><div>' + content.sun   + '</div></li>'
        html += '<li><div class="li-left">' + str(weekdays[5].month)+'/'+str(weekdays[5].day)+'(月)</div><div>' + content.mon   + '</div></li>'
        html += '<li><div class="li-left">' + str(weekdays[6].month)+'/'+str(weekdays[6].day)+'(火)</div><div>' + content.tues  + '</div></li>'
        html += '</ul><h1>・所感, 次週までの感想</h1><p>'
        html += content.journal
        html += '</p></main></div></body></html>'
        # print(html)
        # PDF出力
        return pdfkit.from_string(html, False, options=options, configuration=config)

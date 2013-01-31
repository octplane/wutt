 # -*- coding:  utf-8 -*-

from django.shortcuts import render


def index(request):
  context = {'mailList' : [
    {'id' : 29503, 'flag' : 'CDT','date' : '23 Jan 2013', 'from' : 'Roger Daniel', 'extra' : 0, 'subject' : 'Scandale ?!'},
    {'id' : 29504, 'flag' : 'CDT','date' : '23 Jan 2013', 'from' : 'Daniel R.', 'extra' : 0, 'subject' : '`->'},
    {'id' : 29505, 'flag' : 'CDT','date' : '23 Jan 2013', 'from' : 'R. dany', 'extra' : 0, 'subject' : '&nbsp;`—>'},
    {'id' : 29506, 'flag' : 'CDT','date' : '23 Jan 2013', 'from' : 'Roger Daniel', 'extra' : 0, 'subject' : ' &nbsp;&nbsp;`->'}

  ]}
  return render(request, 'index.html', context)

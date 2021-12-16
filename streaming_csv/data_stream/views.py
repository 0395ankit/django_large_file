from django.shortcuts import render

# Create your views here.
import csv
from django.http import StreamingHttpResponse


def index_view(request):
    context={}
    return render(request, 'index.html', context)


class DummyFile:
    def write(self, value_to_write):
        return value_to_write


def large_csv(request):
    rows = ([str(i), str(2 * i), str(3 * i)] for i in range(1000))
    writer = csv.writer(DummyFile())
    data = [writer.writerow(row) for row in rows]
    response = StreamingHttpResponse(data, content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename="pythoncircle-dot-com.csv"'
    return response
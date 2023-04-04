from django.shortcuts import redirect
from rest_framework.generics import ListCreateAPIView
from shortener.models import ShortenerModel
from shortener.serializer import ShortenerSerializer

# Create your views here.

class ShortenerView(ListCreateAPIView):
    serializer_class = ShortenerSerializer
    queryset = ShortenerModel.objects.all().order_by('-views')[:100]

def ShortenerRedirect(request, encoded):
    try:
        shortend = ShortenerModel.objects.get(encoded=encoded)
        if not shortend:
            return redirect('/')
        shortend.views = shortend.views + 1
        shortend.save()
        return redirect(shortend.source_url)
    except:
        return redirect('/')
from weather_display.models import Station, Reading
from rest_framework import viewsets
from rest_framework import permissions
from weather_display.serializers import ReadingSerializer, StationSerializer
from django.views.generic import TemplateView


class StationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows stations to be viewed or edited.
    """
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    permission_classes = [permissions.IsAuthenticated]


class ReadingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows readings to be viewed or edited.
    """
    queryset = Reading.objects.all().order_by('-timestamp')
    serializer_class = ReadingSerializer
    permission_classes = [permissions.IsAuthenticated]


class PageView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class LandingView(PageView):
    template_name = "landing.html"

    def dispatch(self, *args, **kwargs):
        response = super(LandingView, self).dispatch(*args, **kwargs)
        return response
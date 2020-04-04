# from covid_gandaki.users.models import User
from rest_framework import routers, serializers, viewsets

from covid_gandaki.snippets.modal_serializers import lb,users,form,food_meds,public
# ViewSets define the view behavior.

class TravelViewSet(viewsets.ModelViewSet):
    queryset = form.Travel.objects.all()
    serializer_class  = form.Lb_Travel_Serializer




class UserViewSet(viewsets.ModelViewSet):
    queryset = users.User.objects.all()
    serializer_class = users.UserSerializer


class ReliefViewSet(viewsets.ModelViewSet):
    queryset = lb.ReliefFund.objects.all()
    serializer_class = lb.ReliefFundSerializer

class HospitalViewSet(viewsets.ModelViewSet):
    queryset = lb.Hospital.objects.all()
    serializer_class = lb.HospitalSerializer

class CovidViewSet(viewsets.ModelViewSet):
    queryset = public.QTPerson.objects.all()
    serializer_class = public.QTPersonSerializer

class NeedyViewSet(viewsets.ModelViewSet):
    queryset = public.Needy.objects.all()
    serializer_class = public.NeedySerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'relief',ReliefViewSet )
router.register(r'quarantines', HospitalViewSet)
router.register(r'travel', TravelViewSet)
router.register(r'covid', CovidViewSet)
router.register(r'needy', NeedyViewSet)

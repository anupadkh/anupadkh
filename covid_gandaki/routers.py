# from covid_gandaki.users.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from covid_gandaki.snippets.modal_serializers import lb,users,form,food_meds,public
# ViewSets define the view behavior.



class TravelViewSet(viewsets.ModelViewSet):
    queryset = form.Travel.objects.all()
    serializer_class  = form.Lb_Travel_Serializer

    @method_decorator(csrf_exempt)
    def create(self, *args, **kwargs):
        return super(TravelViewSet, self).create(*args, **kwargs)

    

    




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

class PetroleumViewSet(viewsets.ModelViewSet):
    queryset = food_meds.Petroleum.objects.all()
    serializer_class = food_meds.Lb_Petroleum_Serializer

class ProductionViewSet(viewsets.ModelViewSet):
    queryset = food_meds.Production.objects.all()
    serializer_class = food_meds.Lb_Production_Serializer

class MedicalViewSet(viewsets.ModelViewSet):
    queryset = food_meds.Medical.objects.all()
    if len(queryset) == 0:
        queryset = [food_meds.Medical()]
    serializer_class = food_meds.Lb_Medical_Serializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'relief',ReliefViewSet )
router.register(r'quarantines', HospitalViewSet)
router.register(r'travel', TravelViewSet)
router.register(r'covid', CovidViewSet)
router.register(r'needy', NeedyViewSet)
router.register(r'medical', MedicalViewSet)
router.register(r'sell', ProductionViewSet)
router.register(r'supplies', PetroleumViewSet)

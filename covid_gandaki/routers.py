# from covid_gandaki.users.models import User
from rest_framework import routers, serializers, viewsets

from covid_gandaki.snippets.modal_serializers import lb,users,form,food_meds,public
# ViewSets define the view behavior.



class UserViewSet(viewsets.ModelViewSet):
    queryset = users.User.objects.all()
    serializer_class = users.UserSerializer


class ReliefViewSet(viewsets.ModelViewSet):
    queryset = lb.ReliefFund.objects.all()
    serializer_class = lb.ReliefFundSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'relief',ReliefViewSet )

# from covid_gandaki.users.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework.permissions import BasePermission, SAFE_METHODS

from covid_gandaki.snippets.modal_serializers import lb,users,form,food_meds,public
# ViewSets define the view behavior.
from rest_framework.decorators import action

 




class TravelViewSet(viewsets.ModelViewSet):
    queryset = form.Travel.objects.all().prefetch_related('traveller')
    serializer_class  = form.Lb_Travel_Serializer

    @action(detail=False, methods=['get'])
    def user(self,request,pk=None):
        # if request.method=='GET':
        #     return Response ({'Hi':'There'})
        # if request.method == 'POST':
        #     return Response({"GO":"Now"})
        employee = users.Employee.objects.get(user=request.user)
        mun = employee.municipality.address.mun
        creators = users.Employee.objects.filter(municipality=employee.municipality).values('user')
        y = form.Travel.objects.filter(created_by__in=creators).prefetch_related('traveller')
        serializer = self.get_serializer(y, many=True)
        return Response(serializer.data)
        # return Response(serializer.data)

    # @action(detail=False)
    # def user(self, request):
    #     serializer = self.get_serializer(
    #         form.Travel.objects.filter(created_by=request.user), many=True)
    #     return Response(serializer.data)


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class MunViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = lb.Municipality.objects.all()
    permission_classes = [ReadOnly] 
    serializer_class = lb.MunicipalitySerializer

    
class DistrictViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = lb.District.objects.all()
    serializer_class = lb.DistrictSerializer
    permission_classes = [ReadOnly]

    @action(detail=True, methods=['get'])
    def mun(self,request,pk=None):
        if pk==None:
            y = lb.Municipality.objects.all()
        else:
            y = lb.Municipality.objects.filter(district=pk)
        
        serializer = lb.MunicipalitySerializer(y,many=True)
        return Response(serializer.data)


    

class DistributerViewSet(viewsets.ModelViewSet):
    queryset = lb.OfficeEmployee.objects.all()
    serializer_class = lb.OfficeEmployeeSerializer

    @action(detail=True, methods=['get'])
    def mun(self,request,pk=None):
        if pk==None:
            y = lb.OfficeEmployee.objects.filter(office__mun=request.user.municipality.mun)
        else:
            y = lb.OfficeEmployee.objects.get(pk=pk)
        serializer = lb.OfficeEmployeeSerializer(y,many=True)
        return Response(serializer.data)


class ReliefDistributerViewSet(viewsets.ModelViewSet):
    queryset = lb.ReliefFund.objects.all()
    serializer_class = lb.ReliefFundSerializer

    @action(detail=False, methods=['get'])
    def mun(self, request, pk=None):
        if pk == None:
            employee = users.Employee.objects.get(user=request.user)
            mun = employee.municipality.address.mun
            y = lb.ReliefFund.objects.filter(
                office__address__mun=mun)
        else:
            y = lb.ReliefFund.objects.get(pk=pk)
        serializer = lb.ReliefFundSerializer(y, many=True)
        return Response(serializer.data)

        





class UserViewSet(viewsets.ModelViewSet):
    queryset = users.User.objects.filter(id__lte = 0)
    serializer_class = users.UserSerializer


class ReliefItemViewSet(viewsets.ModelViewSet):
    receivers = lb.ReliefItem.objects.all().values_list('receiver', flat=True)
    queryset = public.Person.objects.filter(id__in=receivers)
    serializer_class = lb.ReliefPersonSerializer

    @action(detail=False, methods=['get'])
    def user(self,request,pk=None, sid=None):
        employee = users.Employee.objects.get(user=request.user)
        if self.kwargs.get('sid', False):
            RI = lb.ReliefItem.objects.filter(
                fund__office__address__mun=employee.municipality.address.mun, fund = self.kwargs['sid'])
        else:
            RI = lb.ReliefItem.objects.filter(
                fund__office__address__mun=employee.municipality.address.mun)
        receivers = RI.values_list('receiver', flat=True)
        y = public.Person.objects.filter(id__in=receivers)
        serializer = lb.ReliefPersonSerializer(y, many=True)
        foodsitems = food_meds.FoodName.objects.filter(
            mun=employee.municipality.address.mun)
        return Response(serializer.data)
    
    def get_queryset(self):
        query = super().get_queryset()
        if self.kwargs.get('sid', False):
            query = query.filter(fund=self.kwargs['sid'])
        return query


        
        
            # employee = users.Employee.objects.get(user=request.user)
            # RI = lb.ReliefItem.objects.filter(
            #     fund__office__address__mun=employee.municipality.address.mun)
            # receivers = RI.values_list('receiver', flat=True)
            # y = public.Person.objects.filter(id__in=receivers)
            # serializer = lb.ReliefPersonSerializer(y, many=True)
            # foodsitems = food_meds.FoodName.objects.filter(
            #     mun=employee.municipality.address.mun)
            
            # return Response({"Guss":"hello"})

    



class ReliefViewSet(viewsets.ModelViewSet):
    queryset = lb.Person.objects.filter(belong_to_form = 4)
    serializer_class = lb.ReliefPersonSerializer

    # @action(detail=False, methods=['get'])
    # def user(self,request, pk=None)

    

class HospitalViewSet(viewsets.ModelViewSet):
    queryset = lb.Hospital.objects.all()
    serializer_class = lb.HospitalSerializer

    @action(detail=False, methods=['get'])
    def user(self, request, pk=None):
        employee = users.Employee.objects.get(user=request.user )
        y = list(lb.Hospital.objects.filter( mun = employee.municipality.address.mun ))
        y.append(lb.Hospital(name="नभएको"))
        serializer = self.get_serializer(y, many=True)
        return Response(serializer.data)


class CovidViewSet(viewsets.ModelViewSet):
    queryset = public.QTPerson.objects.all()
    serializer_class = public.QTPersonSerializer

    @action(detail=False, methods=['get'])
    def user(self, request, pk=None):
        employee = users.Employee.objects.get(user=request.user)
        mun = employee.municipality.address.mun
        hospitals = lb.Hospital.objects.filter(mun = mun)
        y = public.QTPerson.objects.filter(person__current_full_address__mun = mun )
        serializer = self.get_serializer(y, many=True)
        return Response(serializer.data)


class NeedyViewSet(viewsets.ModelViewSet):
    queryset = public.Needy.objects.all()
    serializer_class = public.NeedySerializer

    @action(detail=False, methods=['get'])
    def user(self, request, pk=None):
        employee = users.Employee.objects.get(user=request.user)
        mun = employee.municipality.address.mun
        y = public.Needy.objects.filter(municipality = mun)
        serializer = self.get_serializer(y, many=True)
        return Response(serializer.data)


    

class PetroleumViewSet(viewsets.ModelViewSet):
    queryset = food_meds.Petroleum.objects.all()
    serializer_class = food_meds.Lb_Petroleum_Serializer

    @action(detail=False, methods=['get'])
    def user(self, request, pk=None):
        employee = users.Employee.objects.get(user=request.user)
        mun = employee.municipality.address.mun
        y = food_meds.Petroleum.objects.filter(demand_by=mun)
        serializer = self.get_serializer(y, many=True)
        return Response(serializer.data)

class ProductionViewSet(viewsets.ModelViewSet):
    queryset = food_meds.Production.objects.all()
    serializer_class = food_meds.Lb_Production_Serializer

    @action(detail=False, methods=['get'])
    def user(self, request, pk=None):
        employee = users.Employee.objects.get(user=request.user)
        mun = employee.municipality.address.mun
        y = food_meds.Production.objects.filter(produced_by=mun)
        serializer = self.get_serializer(y, many=True)
        return Response(serializer.data)

class MedicalViewSet(viewsets.ModelViewSet):
    queryset = food_meds.Medical.objects.all()
    serializer_class = food_meds.Lb_Medical_Serializer

    @action(detail=False, methods=['get'])
    def user(self, request, pk=None):
        employee = users.Employee.objects.get(user=request.user)
        mun = employee.municipality.address.mun
        y = food_meds.Medical.objects.filter(produced_by=mun)
        serializer = self.get_serializer(y, many=True)
        return Response(serializer.data)

class FoodNameViewSet(viewsets.ModelViewSet):
    queryset = food_meds.FoodName.objects.all()
    serializer_class = food_meds.Lb_FoodName

    @action(detail=False, methods=['get'])
    def user(self, request, pk=None):
        employee = users.Employee.objects.get(user=request.user)
        mun = employee.municipality.address.mun
        y = food_meds.FoodName.objects.filter(mun=mun)
        serializer = self.get_serializer(y,many=True)
        return Response(serializer.data)

class OfficeViewSet(viewsets.ModelViewSet):
    queryset = lb.Office.objects.all()
    serializer_class = lb.OfficeSerializer

    @action(detail=False, methods=['get'])
    def user(self, request, pk=None):
        employee = users.Employee.objects.get(user=request.user)
        mun = employee.municipality.address.mun
        y = lb.Office.objects.filter(address__mun=mun)
        serializer = self.get_serializer(y, many=True)
        return Response(serializer.data)

    


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'quarantines', HospitalViewSet)
router.register(r'travel', TravelViewSet)
router.register(r'covid', CovidViewSet)
router.register(r'needy', NeedyViewSet)
router.register(r'medical', MedicalViewSet)
router.register(r'sell', ProductionViewSet)
router.register(r'supplies', PetroleumViewSet)
router.register(r'district', DistrictViewSet)
# router.register(r'travels', FooView.asView())

router.register(r'relief',ReliefViewSet )
router.register(r'reliefdistributers', ReliefDistributerViewSet)
router.register(r'relieffoodname', FoodNameViewSet)
router.register(r'reliefItem', ReliefItemViewSet)
router.register(r'myObjects/(?P<sid>\d+)', ReliefItemViewSet)
router.register(r'reliefOffice', OfficeViewSet)
router.register(r'muns', MunViewSet)

class ColumnSize(viewsets.ModelViewSet):
    queryset = form.ColumnSize.objects.all()
    serializer_class = form.ColumnSizeSerializer

    @action(detail=False, methods=['get', 'post'], url_path='column', url_name='column_user')
    def user(self, request, table=None):
        employee = users.Employee.objects.get(user=request.user)
        mun = employee.municipality.address.mun
        if request.method == "POST":
            data = request.data
            column = form.ColumnSize.objects.get_or_create(table_name= data['file'], mun=mun)[0]
            column.column_size = str(data['column'])
            # column.is_valid()
            column.save()
            return Response(form.ColumnSizeSerializer(column).data)
        elif request.method == "GET":
            # table = request.data['table']
            query, status = form.ColumnSize.objects.get_or_create(mun=mun, table_name = table)
            queryset = form.ColumnSizeSerializer(query, many=False)
            return Response(queryset.data)


router.register(r'columnSize', ColumnSize)
router.register(r'column/(?P<table>\w+)', ColumnSize)

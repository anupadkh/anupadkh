from django.urls import path
from django.conf.urls import include, url
from covid_gandaki.form import views as fv
import covid_gandaki.users.views as uv
import covid_gandaki.form.dash_view as dv

urlpatterns=[
    path('', uv.landing, name='landing' ),
    path('myindex', fv.index, name='index'),
    path('submission', fv.submit_general, name='submit'),
    path('muns/', fv.mun_list, name="muns"),
    path('test/', fv.test, name="test"),
    path('<int:id>/dtable/', fv.datatable, name="datatable"),
    path('lbindex/', fv.lb_index, name="lbindex"),
    path('<int:id>/log_tables/', dv.create_dashboard, name="staff_board"),
]

app_name = "form"

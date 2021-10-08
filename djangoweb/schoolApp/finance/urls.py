from django.urls import path

from finance.views import feeCollection;
from finance.views import feeDueReport;
from finance.views import feeCollectionReport;


urlpatterns = [
    path('feecoll/', feeCollection),
    path('duesreport/', feeDueReport),
    path('collectionreport/',feeCollectionReport),

]

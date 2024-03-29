from django.urls import include, path

from .api_urls import package_router
from .views import IndexView
from .api_views import WagyuInfomationAPIView

app_name = "wagyuer"

api_urlpatterns = [
    path("packages/", include(package_router.urls)),
    path("wagyuId/", WagyuInfomationAPIView.as_view()),
]

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path(
        "api/0.1/",
        include(api_urlpatterns),
        name="api_package",
    ),
]

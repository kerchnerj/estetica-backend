from django.contrib import admin
from django.urls import include, path
from usuario.router import router as usuario_router
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from uploader.router import router as uploader_router


from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from estetica.views import (
    AgendamentoViewSet,
    ClienteViewSet,
    PacoteViewSet,
    ProcedimentoViewSet,
    PacotesProcessoViewSet,
)


router = DefaultRouter()
router.register(r"pacotesprocesso", PacotesProcessoViewSet)
router.register(r"pacote", PacoteViewSet)
router.register(r"agendamento", AgendamentoViewSet)
router.register(r"procedimento", ProcedimentoViewSet)
router.register(r"cliente", ClienteViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/usuario", include(usuario_router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("api/media/", include(uploader_router.urls)),
]
urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
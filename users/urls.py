from users.apps import UsersConfig
from rest_framework.routers import SimpleRouter

app_name = UsersConfig.name

router = SimpleRouter()

urlpatterns = []

urlpatterns += router.urls

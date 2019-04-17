

from . views import QuestionViewSet, ChoiceViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', QuestionViewSet, base_name='questions')
urlpatterns = router.urls

router = DefaultRouter()
router.register('', ChoiceViewSet, base_name='choices')
urlpatterns = router.urls

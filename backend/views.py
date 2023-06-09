from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Core
from .serializers import CoreSerializer

@api_view(['GET'])
def call_click(request):
    core = Core.objects.get(user=request.user)
    is_levelup = core.click()
    if is_levelup:
        Boost.objects.create(core=core, price=price.level*50, power=core.level*20)
    core.save()

    return Response({'core': CoreSerializer(core).data, 'is_levelup' : is_levelup})


class BoostViewSet(viewset.ModelViewset):
    queryset = Boost.objects.all()
    serializer_class = BoostSerializer

    def get_queryset(self):
        core = Core.objects.get(user=self.request.user)
        boosts = Boost.objects.filter(core=core)
        return boosts

def index(request):
    coreModel = apps.get_model('backend', 'Core')
    boostsModel = apps.get_model('backend', 'Boost')
    core = coreModel.object.get(user=request.user)
    boosts = boostsModel.object.filter(core=core)

    return render(request, 'index.html', {
        'core': core,
        'boosts': boosts,
    })
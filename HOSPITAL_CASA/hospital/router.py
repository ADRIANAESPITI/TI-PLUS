from hospitalApp.viewsets import PacienteViewset, FamiliarViewset, MedicoViewset, AuxiliarViewset, Historia_clinicaViewset, Signos_vitalesViewset, SugerenciaViewset, AsignacionViewset
from rest_framework import routers

router=routers.DefaultRouter()
router.register('paciente', PacienteViewset)

router = routers.DefaultRouter()
router.register('familiar', FamiliarViewset)

router = routers.DefaultRouter()
router.register('medico', MedicoViewset)

router = routers.DefaultRouter()
router.register('auxiliar', AuxiliarViewset)

router = routers.DefaultRouter()
router.register('historia_clinica', Historia_clinicaViewset)

router = routers.DefaultRouter()
router.register('signos_vitales', Signos_vitalesViewset)

router = routers.DefaultRouter()
router.register('sugerencia', SugerenciaViewset)

router = routers.DefaultRouter()
router.register('asignacion', AsignacionViewset)

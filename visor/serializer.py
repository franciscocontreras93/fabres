from django.core.serializers import serialize

class FabresSerializer():
    
    def PublicSerializer(queryset):
        fieldsPublic = ['nom_ccpp','idmanzana','departamen','provincia','distrito','hombre','mujer','pob_total','propor_nbi','q_propnbi','geom']
        return serialize('geojson', queryset, fields = (fieldsPublic))

    def PrivateSerializer(queryset):
        return serialize('geojson', queryset)

    def TestingSerializer(queryset):
        fieldsTesting = ['nom_ccpp','idmanzana','departamen','provincia','distrito','hombre','mujer','pob_total']
        return serialize('json', queryset, fields = (fieldsTesting))


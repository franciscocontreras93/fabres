from django.core.serializers import serialize

class FabresSerializer():
    
    def BaseSerializer(queryset): 
        fieldsBase = [
            'distrito',
            'geom'
        ]
        return serialize('geojson', queryset, fields=(fieldsBase))

    def PublicSerializer(queryset):
        fieldsPublic = ['idmanzana',
                        'departamen',
                        'provincia',
                        'distrito',
                        'nom_ccpp',
                        'hombre',
                        'mujer',
                        'pob_total',
                        'f0_a_14',
                        'f15_a_29',
                        'f30_a_59',
                        'f60_a_mas',
                        'q_propnbi',
                        'q_mcalor',
                        'q_mercado',
                        'p_mcalor',
                        'area_ha',
                        'q_30_a_59',
                        'q_pob60',
                        'q_densid',
                        'n_riesgo',
                        'geom']
        return serialize('geojson', queryset, fields = (fieldsPublic))

    def PrivateSerializer(queryset):
        return serialize('geojson', queryset)

    def TestingSerializer(queryset):
        fieldsTesting = ['nom_ccpp','idmanzana','departamen','provincia','distrito','hombre','mujer','pob_total']
        return serialize('json', queryset, fields = (fieldsTesting))

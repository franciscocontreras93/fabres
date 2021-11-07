from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import DistritosModel 


# Auto-generated `LayerMapping` dictionary for DistritosModel model
distritosmodel_mapping = {
    'fid': 'fid',
    'nom_ccpp': 'nom_ccpp',
    'idmanzana': 'idmanzana',
    'id_manzana': 'id_manzana',
    'departamen': 'departamen',
    'provincia': 'provincia',
    'distrito': 'distrito',
    'hombre': 'hombre',
    'mujer': 'mujer',
    'pob_total': 'pob_total',
    'ubigeo': 'ubigeo',
    'f0_a_14': 'f0_a_14',
    'f15_a_29': 'f15_a_29',
    'f60_a_mas': 'f60_a_mas',
    'f30_a_59': 'f30_a_59',
    'pob_nbi': 'pob_nbi',
    'pob_midis': 'pob_midis',
    'propor_nbi': 'propor_nbi',
    'q_propnbi': 'q_propnbi',
    'p_propnbi': 'p_propnbi',
    'area_ha': 'area_ha',
    'dens_pob': 'dens_pob',
    'q_pob60': 'q_pob60',
    'p_pob60': 'p_pob60',
    'q_30_a_59': 'q_30_a_59',
    'p_30_a_59': 'p_30_a_59',
    'q_densid': 'q_densid',
    'p_densid': 'p_densid',
    'q_mcalor': 'q_mcalor',
    'p_mcalor': 'p_mcalor',
    'q_mercado': 'q_mercado',
    'p_mercado': 'p_mercado',
    'v_descen': 'v_descen',
    'v_condic': 'v_condic',
    'v_susc': 'v_susc',
    'v_eexp': 'v_eexp',
    'v_riesgo': 'v_riesgo',
    'n_riesgo': 'n_riesgo',
    'geom': 'MULTIPOLYGON',
}

distritos_shp = Path(__file__).resolve().parent / 'data' / 'distritos.shp'

def run(verbose=True):
    lm = LayerMapping(DistritosModel, distritos_shp, distritosmodel_mapping, transform=False)
    lm.save(strict=True,verbose=verbose)


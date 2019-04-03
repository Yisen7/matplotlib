from pygal_maps_world.i18n import COUNTRIES


def get_country_code(country_name):
    # 根据指定国家名称，返回两位国别码
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        # 未找到制定国家，返回None
    return None

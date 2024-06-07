import pandas as pd
def convertir_archivo():
    """ Lee el archivo ecxel y me devuelve una lista de diccionarios """
    # Ruta del archivo Excel
    ruta_excel = r'app/datosEspecies.xlsx'

    # Cargar el archivo Excel
    excel = pd.ExcelFile(ruta_excel)

    # Leer la primera hoja del archivo Excel
    df = excel.parse(excel.sheet_names[0])

    # Eliminar espacios en blanco de las celdas
    df = df.map(lambda x: x.strip() if isinstance(x, str) else x)

    # Reemplazar cadenas vacías con NaN
    df.replace("", pd.NA, inplace=True)

    # Convertir las columnas de fecha y hora, si las hay
    for col in df.columns:
        if 'fecha' in col.lower() or 'date' in col.lower():
            df[col] = pd.to_datetime(df[col], errors='coerce')

    # Eliminar filas y columnas completamente vacías
    df.dropna(how='all', inplace=True)
    df.dropna(axis=1, how='all', inplace=True)

    data_list = df.to_dict(orient='records')

    return data_list


def filterData(keyFilter):
    data_list = convertir_archivo()
    print(keyFilter)
    # Filtro de especies
    list_filter = list(filter(lambda item: any(keyFilter in str(value).lower() for value in item.values()), data_list))
    return list_filter

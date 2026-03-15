from base_functions import explode_on, normalize_column, split_on, from_timestampms_to_datetime

CONFIG = [
    {
        "url": "https://www.google.com/maps/d/kml?mid=1B2OWELqpzGee7_NO9SgzeDXf966YrYs",
        "format": "kmz",
        "disambiguator": "Serra - ES -",
        "data_format_config": {
            "columns": ["Name", "geometry", "description"],
            "layers": ["IMPRÓPRIO", "PRÓPRIO"]
        },
        "mappings": {
            "Name": "id",
            "geometry": "location",
            "date": "date",
            "status": "status",
        },
        "status_mapping": {
            "IMPRÓPRIO": "IMPROPER",
            "PRÓPRIO": "PROPER"
        },
        "transforms": [
            {
                "function": split_on,
                "column": "description",
                "output": "entries",
                "split_string": "<br>",
                "expand": False
            },
            {
                "function": explode_on,
                "column": "entries",
            },
            {
                "function": split_on,
                "column": "entries",
                "output": ["date", "status"],
                "split_string": " - ",
                "expand": True
            },
        ]
    },
    {
        "url": "https://www.google.com/maps/d/kml?mid=1fBWO4Jm2j23dgMMG-GIN7zCuWKbGQlBZ&resourcekey&lid=00wi8bi5-X8",
        "format": "kmz",
        "disambiguator": "Aracruz - ES -",
        "data_format_config": {
            "layers": None,
            "columns": ["geometry", "Name", "Situa____o", "Data_da___ltima_Coleta"]
        },
        "mappings": {
            "Name": "id",
            "geometry": "location",
            "Data_da___ltima_Coleta": "date",
            "Situa____o": "status"
        },
        "status_mapping": {
            "IMPRÓPRIO": "IMPROPER",
            "PRÓPRIO": "PROPER"
        },
        "transforms": []
    },
    {
        "url": "https://arcgis.cetesb.sp.gov.br/server/rest/services/Hosted/Praias/FeatureServer/0/query?where=1%3D1&fullText=&objectIds=&uniqueIds=&time=&geometry=&geometryType=esriGeometryPoint&inSR=&defaultSR=&spatialRel=esriSpatialRelIntersects&distance=&units=esriSRUnit_Foot&relationParam=&outFields=praia%2Cdata_amostra_inicio%2Cclassificacao_texto&returnGeometry=true&maxAllowableOffset=&geometryPrecision=&outSR=&havingClause=&gdbVersion=&historicMoment=&returnDistinctValues=false&returnIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&multipatchOption=xyFootprint&resultOffset=&resultRecordCount=&returnTrueCurves=false&returnCentroid=false&timeReferenceUnknownClient=false&maxRecordCountFactor=&sqlFormat=none&resultType=&datumTransformation=&lodType=geohash&lod=&lodSR=&cacheHint=false&returnUniqueIdsOnly=false&f=pjson",
        "format": "json",
        "disambiguator": "São Paulo -",
        "data_format_config": {
            "path_to_array": ["features"],
            "path_to_attributes": ["attributes"],
            "lat_path": ["geometry", "y"],
            "lng_path": ["geometry", "x"]
        },
        "mappings": {
            "praia": "id",
            "geometry": "location",
            "data_amostra_inicio": "date",
            "classificacao_texto": "status"
        },
        "status_mapping": {
            "Imprópria": "IMPROPER",
            "Própria": "PROPER"
        },
        "transforms": [{
            "function": from_timestampms_to_datetime,
            "field": "data_amostra_inicio"
        }]
    }
]

TEST_CONFIG = [
    {
        "url": "https://balneabilidade.ima.sc.gov.br/relatorio/mapa",
        "format": "json",
        "disambiguator": "São Paulo -",
        "data_format_config": {
            "path_to_array": [],
            "path_to_attributes": [],
            "lat_path": ["LATITUDE"],
            "lng_path": ["LONGITUDE"]
        },
        "mappings": {
            "BALNEARIO": "id",
            "location": "location",
            "DATA": "date",
            "CONDICAO": "status"
        },
        "status_mapping": {
            "IMPRÓPRIO": "IMPROPER",
            "PRÓPRIO": "PROPER"
        },
        "transforms": [
            {
                "function": explode_on,
                "column": "ANALISES",
            },
            {
                "function": normalize_column,
                "column": "ANALISES",
            }
        ]
    }
]
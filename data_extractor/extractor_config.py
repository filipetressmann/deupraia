from base_functions import explode_on, normalize_column, split_on, from_timestampms_to_datetime
from power_bi_parser import parse_power_bi_data

CONFIG = [
    {
        "url": "https://www.google.com/maps/d/kml?mid=1B2OWELqpzGee7_NO9SgzeDXf966YrYs",
        "format": "kmz",
        "disambiguator": "Espirito Santo -",
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
        "disambiguator": "Espirito Santo -",
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
            "Imprópria": "IMPROPER",
            "Própria": "PROPER"
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
            "location": "location",
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
    },
    {
        "url": "https://balneabilidade.ima.sc.gov.br/relatorio/mapa",
        "format": "json",
        "disambiguator": "Santa Catarina - ",
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
    },
    {
        "url": "https://wabi-brazil-south-api.analysis.windows.net/public/reports/querydata?synchronous=true",
        "path": "./payloads/rj",
        "format": "json",
        "disambiguator": "Rio de Janeiro -",
        "parser": parse_power_bi_data,
        "data_format_config": {
            "path_to_array": ["results", 0, "result", "data", "dsr", "DS", 0, "PH", 0, "DM0"],
            "path_to_attributes": [],
            "lat_path": [1],
            "lng_path": [2]
        },
        "mappings": {
            "3": "id",
            "location": "location",
            "4": "date",
            "0": "status"
        },
        "status_mapping": {
            "Imprópria": "IMPROPER",
            "Própria": "PROPER"
        },
        "transforms": [{
            "function": from_timestampms_to_datetime,
            "field": "4"
        }]
    },
    {
        "url": "https://wabi-brazil-south-b-primary-api.analysis.windows.net/public/reports/querydata",
        "path": "./payloads/es/vila-velha",
        "format": "json",
        "disambiguator": "Espirito Santo -",
        "parser": parse_power_bi_data,
        "data_format_config": {
            "path_to_array": ["results", 0, "result", "data", "dsr", "DS", 0, "PH", 0, "DM0"],
            "path_to_attributes": [],
            "lat_path": [1],
            "lng_path": [2]
        },
        "mappings": {
            "3": "id",
            "location": "location",
            "4": "date",
            "0": "status"
        },
        "status_mapping": {
            "Sist. Imprópria": "IMPROPER",
            "IMPRÓPRIA": "IMPROPER",
            "PRÓPRIA": "PROPER"
        },
        "transforms": [{
            "function": from_timestampms_to_datetime,
            "field": "4"
        }]
    }
]

TEST_CONFIG = [
    {
        "url": "https://balneabilidade.ima.sc.gov.br/relatorio/mapa",
        "format": "json",
        "disambiguator": "Santa Catarina - ",
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
import requests

def requestAPI(date: int):
    URL = 'https://open.neis.go.kr/hub/mealServiceDietInfo'
    param = { "ATPT_OFCDC_SC_CODE" : "R10",
              "SD_SCHUL_CODE" : 8801139,
              "Type" : "json",
              "MLSV_YMD" : date}
    responce = requests.get(URL, param)
    return responce.json()
"""
@author : Tej Prakash Sharma
Class used to handle Json
"""
import json


class JsonHelper:

    def readJson(jsonPath):
        with open(jsonPath, 'r') as file:
            credentials = json.load(file)
        return credentials

    def writeJson(jsonPath, data):
        with open(jsonPath, 'w') as file:
            Data = json.dump(data, file)
        return Data


from pydantic import BaseModel
from pydantic.fields import Field
from pydantic.networks import EmailStr
from typing import List, Optional

class User(BaseModel):
    userID: int=Field(...)
    name: Optional[str]
    email: Optional[EmailStr]
    username: str=Field(...)
    password: str=Field(...)
    listOfProjects: Optional[List[int]]

    class Config:
        arbitrary_types_allowed=True
        allow_population_by_field_name=True
        schema_extra={
            "example":{
                "userID":101,
                "name": "John Doe",
                "email": "johndoe@email.com",
                "username": "TheJohnDoe",
                "password": "password@Super@Secure",
                "listOfProjects": [45,43,22]
            }
        }

class UpdateUser(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    listOfProjects: Optional[List[int]]

    class Config:
        arbitrary_types_allowed=True
        allow_population_by_field_name=True
        schema_extra={
            "example":{
                "name": "John Doe",
                "email": "johndoe@email.com",
                "listOfProjects": [45,43,22]
            }
        }

class Project(BaseModel):
    projectID:int=Field(...)
    projectName:Optional[str]
    rawDataPath: Optional[str]
    projectFolderPath: Optional[str]
    belongsToUserID: int=Field(...)
    listOfDataIDs: Optional[List[int]]
    autoConfigFileLocation: Optional[str]
    plotsPath: Optional[str]
    projectType: Optional[str]
    isAuto: Optional[bool]
    target: Optional[str]

    class Config:
        arbitrary_types_allowed=True
        allow_population_by_field_name=True
        schema_extra={
            "example":{
                "projectID": 45,
                "projectName": "Boston Housing",
                "rawDataPath": "/path/to/data/rawfile.csv",
                "projectFolderPath": "/path/to/data",
                "belongsToUserID": 101,
                "listOfDataIDs": [2,4],
                "autoConfigFileLocation": "path/to/auto/config/file.yaml",
                "plotsPath": "path/to/plot/file.html",
                "projectType":"regression",
                "isAuto": "true",
                "target": "target"
            }
        }

class UpdateProject(BaseModel):
    projectName:Optional[str]
    rawDataPath: Optional[str]
    projectFolderPath: Optional[str]
    listOfDataIDs: Optional[List[int]]

    class Config:
        arbitrary_types_allowed=True
        allow_population_by_field_name=True
        schema_extra={
            "example":{
                "projectName": "Boston Housing",
                "rawDataPath": "/path/to/data/rawfile.csv",
                "projectFolderPath" : "path/to/data",
                "listOfDataIDs": [2,4]
            }
        }

class Data(BaseModel):
    dataID: int=Field(...)
    cleanDataPath: Optional[str]
    target: Optional[str]
    belongsToUserID: int=Field(...)
    belongsToProjectID: int=Field(...)

    class Config:
        arbitrary_types_allowed=True
        allow_population_by_field_name=True
        schema_extra={
            "example":{
                "dataID": 2,
                "cleanDataPath": "/path/to/data/cleanfile.csv",
                "target": "TargetColumnName",
                "belongsToUserID": 101,
                "belongsToProjectID": 45
            }
        }

class UpdateData(BaseModel):
    cleanDataPath: Optional[str]
    target: Optional[str]

    class Config:
        arbitrary_types_allowed=True
        allow_population_by_field_name=True
        schema_extra={
            "example":{
                "cleanDataPath": "/path/to/data/cleanfile.csv",
                "target": "TargetColumnName"
            }
        }


class Model(BaseModel):
    modelID: int=Field(...)
    modelName: Optional[str]='Default Model'
    modelType: Optional[str]
    pickleFolderPath: Optional[str]
    pickleFilePath: Optional[str]
    belongsToUserID: int=Field(...)
    belongsToProjectID: int=Field(...)
    belongsToDataID: Optional[int]

    class Config:
        allow_population_by_field_name=True
        arbitrary_types_allowed=True
        schema_extra={
            "example":{
                "modelID": 13,
                "modelName": "Linear Regression",
                "modelType": "Default Model",
                "pickleFolderPath": "/path/to/pickel/data/",
                "pickleFilePath": "/path/to/pickle/data/model.pkl",
                "belongsToUserID": 101,
                "belongsToProjectID": 45,
                "belongsToDataID": 2
            }
        }

class UpdateModel(BaseModel):
    modelName: Optional[str]='Default Model'
    modelType: Optional[str]
    picklePath: Optional[str]

    class Config:
        allow_population_by_field_name=True
        arbitrary_types_allowed=True
        schema_extra={
            "example":{
                "modelName": "Linear Regression",
                "modelType": "Regression",
                "picklePath": "/path/to/pickle/data/model.pkl"
            }
        }

class Metrics(BaseModel):
    belongsToUserID: int=Field(...)
    belongsToProjectID: int=Field(...)
    belongsToModelID: int=Field(...)
    addressOfMetricsFile: str=Field(...)

    class Config:
        allow_population_by_field_name=True
        arbitrary_types_allowed=True
        schema_extra={
            "example":{
                "belongsToUserID": 101,
                "belongsToProjectID": 45,
                "belongsToModelID": 13,
                "addressOfMetricsFile": "/path/to/file/metrics.csv"
            }
        }

class InferenceCollection(BaseModel):
    newData: Optional[str]    #address
    results: Optional[str]    #yaml file
    belongsToUserID: int=Field(...)
    belongsToProjectID: int=Field(...)
    belongsToModelID: int=Field(...)

    class Config:
        allow_population_by_field_name=True
        arbitrary_types_allowed=True
        schema_extra={
            "example":{
                "newData": "/path/to/new/inference/data.csv",
                "results": "/path/to/results",
                "belongsToUserID": 101,
                "belongsToProjectID": 45,
                "belongsToModelID": 13
            }
        }

class AutoFormData(BaseModel):
    isauto:Optional[bool]
    target:Optional[str]
    modelnumber:Optional[int]
    nulltype:Optional[str]
    projectID: Optional[int]
    userID: Optional[int]
    clusteringType: Optional[str]

    class Config:
        arbitrary_types_allowed=True
        allow_population_by_field_name=True
        schema_extra={
            "examples":{
                "isauto":True,
                "target":"TargetColumn",
                "modelnumber":2,
                "nulltype":"NA",
                "projectID": 45,
                "userID": 101,
                "clusteringType": "kmeans"
            }
        }

class TimeseriesFormData(BaseModel):
    userID:int
    projectID:int
    target:str
    dateColumn:str
    frequency:str

    class Config:
        arbitrary_types_allowed=True
        allow_population_by_field_name=True
        schema_extra={
            "examples":{
                "userID": "101",
                "projectID": "45",
                "target": "TargetColumn",
                "dateColumn": "DateColumn",
                "frequency": "Frequency"
            }
        }

class PreprocessJSONFormData(BaseModel):
    raw_data_address: Optional[str]
    date_format: Optional[str]
    date_index: Optional[str]
    frequency: Optional[str]
    target_column_name: Optional[str]
    drop_column_name: Optional[List[str]]
    imputation_column_name: Optional[List[str]]
    impution_type: Optional[List[str]]
    mean_median_mode_values: Optional[List[int]]
    na_notation: Optional[List[str]]
    scaling_column_name: Optional[List[str]]
    scaling_type: Optional[List[str]]
    scaling_vales: Optional[List[int]]
    encode_column_name: Optional[List]
    encoding_type:Optional[List]
    labels: Optional[List[str]]
    Remove_outlier: Optional[bool]
    feature_selection: Optional[bool]
    data_imbalance: Optional[bool]
    split_ratio_test: Optional[int]
    is_auto: Optional[bool]
    clean_data_address: Optional[str]
    userID: Optional[int]
    projectID: Optional[int]

    class Config:
        arbitrary_types_allowed=True
        allow_population_by_field_name=True
        schema_extra={
            "examples":{
                "raw_data_address": "path/to/raw/data/file.csv",
                "date_format": "%Y-%m-%d",
                "date_index": "",
                "frequency": "",
                "target_column_name": "target",
                "drop_column_name": [
                    "column_name1",
                    "column_name2",
                    "column_name3"
                ],
                "imputation_column_name": [
                    "column_name1",
                    "column_name2",
                    "column_name3"
                ],
                "impution_type": [
                    "type1",
                    "type2"
                ],
                "mean_median_mode_values": [
                    0,
                    0,
                    0
                ],
                "na_notation": [
                    "NaN"
                ],
                "scaling_column_name": [
                    "age",
                    "sex",
                    "salery"
                ],
                "scaling_type": [
                    "s -mi -ma",
                    "n",
                    "s"
                ],
                "scaling_values": [
                    1,
                    1
                ],
                "encode_column_name": [
                    "encoded_column1"
                ],
                "encoding_type": [
                    "encoding_type"
                ],
                "labels": [
                    "label"
                ],
                "Remove_outlier": True,
                "feature_selection": True,
                "data_imbalance": False,
                "split_ratio_test": 0.3,
                "is_auto": True,
                "clean_data_address":"/path/to/clean/data.csv",
                "userID": 101,
                "projectID":45
                }
        }
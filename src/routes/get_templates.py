from datetime import datetime
from fastapi import APIRouter, HTTPException, Depends, Body
from sqlalchemy.orm import Session
from pydantic import BaseModel
from fastapi.param_functions import Query
from typing import Optional
from db.models import get_session
from loguru import logger

# Below dict is to verify the provided dict contains following keys or not while uploading the Templates
template_base_keys = {"template_id": 1, "version": 1, "name": 1, "class_code": 1, "sub_class_code": 1,
                      "connection_param": 1, "extra_base_param": 1}
template_zone_keys = {"id": 1, "master_template_id": 1, "class_code": 1, "sub_class_code": 1, "connection_param": 1,
                      "measurement": 1, "zone": 1, "zone_name": 1, "zone_type": 1, "enable": 1, "interval_param": 1,
                      "local_storage_enable": 1, "cloud_storage_enable": 1, "rt_enable": 1, "overflow_param": 1,
                      "alarm_param": 1, "min_value": 1, "max_value": 1, "hysteresis": 1, "multiplier": 1,
                      "zone_param": 1, "is_writable": 1, "writable_param": 1, "extra_zone_param": 1}
router = APIRouter()


@router.get('/get_templates_json/', tags=['Templates'])
def get_json_templates():
    try:
        pass
    except Exception as e:
        logger.error(f"Error in get templates: {e}")


@router.post('/add_templates_json/', tags=['Templates'])
def add_json_templates(data: list = Body(...)):
    try:
        db = get_session()
        for templates_ in data:
            for each_param in templates_:
                if each_param in template_base_keys.keys():
                    pass
                else:
                    if each_param == "zones":
                        for each_zone_param in templates_.get(each_param):
                            if each_zone_param in template_zone_keys.keys():
                                pass
    except Exception as e:
        logger.error(f"Error in Add templates: {e}")



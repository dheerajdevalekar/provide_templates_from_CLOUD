# provide_templates_from_CLOUD
This is cloud side API, it will provide the templates according to template_id(int), and template_version(str) in json format.

Below the Base Template Format is There.
```
[
	{
		"template_id": 1,
		"version": "1.1",
		"name": "Selec Energy Meter",
		"class_code": "MOD",
		"sub_class_code": "MOD-EM",
		"connection_param": "{'port': '/dev/serial0', 'baudrate': 9600, 'bytesize': 8, 'parity': 'N'}",
		"interval_param": "{'poll_interval': 10, 'save_interval': 10}",
		"local_storage_enable": true,
		"cloud_storage_enable": true,
		"rt_enable": true,
		"extra_base_param": "{}",
		"zone_parameters": [
			{
				"master_template_id": 1,
				"class_code": "MOD",
				"sub_class_code": "MOD-EM",
				"measurement": "voltage",
				"zone": "V1",
				"zone_name": "Voltage Line1 To Ground",
				"zone_type": "analog",
				"enable": true,
				"interval_param": "{'poll_interval': 10, 'save_interval': 10}",
				"local_storage_enable": true,
				"cloud_storage_enable": true,
				"rt_enable": true,
				"overflow_param": "{}",
				"alarm_param": "{}",
				"min_value": 0.0,
				"max_value": 500.0,
				"hysteresis": 0,
				"multiplier": 1.0,
				"zone_param": "{batches': [], 'register_type': 'input'}",
				"is_writable": false,
				"writable_param": "{}",	
			},
			{
				"master_template_id": 1,
				"class_code": "MOD",
				"sub_class_code": "MOD-EM",
				"measurement": "voltage",
				"zone": "V12",
				"zone_name": "Voltage Line1 To Line2",
				"zone_type": "analog",
				"enable": true,
				"interval_param": "{'poll_interval': 10, 'save_interval': 10}",
				"local_storage_enable": true,
				"cloud_storage_enable": true,
				"rt_enable": true,
				"overflow_param": "{}",
				"alarm_param": "{}",
				"min_value": 0.0,
				"max_value": 500.0,
				"hysteresis": 0,
				"multiplier": 1.0,
				"zone_param": "{batches': [], 'register_type': 'holding'}",
				"is_writable": false,
				"writable_param": "{}",	
			}
		]
	}
]
```
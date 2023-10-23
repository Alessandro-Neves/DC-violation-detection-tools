import pandas

from dcd.core.dc_reader import DCReader
from dcd.duck.dc_detector import DCDetector as DuckDCDetector
# from dcd.duck.dc_detector_verifier import DCDetectorVerifier as DuckDCDetector

from dcd.tools.dataset_operations import DatasetOps

ROOT_PATH = 'testdatas'

configs = [
  # {'dataset': 'employees_40000.csv', 'dcs': ['employees_dc.txt']},
  # {'dataset': 'tax_1000000.csv', 'dcs': ['tax_dc1.txt', 'tax_dc2.txt', 'tax_dc3.txt', 'tax_dc4.txt']},
  # {'dataset': 'lineitem_250000.csv', 'dcs': ['lineitem_dc1.dc']},
  # {'dataset': 'lineorder_1000000.csv', 'dcs': ['lineorder_dc1.txt']},
  # {'dataset': 'flights_18000.csv', 'dcs': ['flights_dc1.dc', 'flights_dc2.dc']},
  {'dataset': 'AdultFull.csv', 'dcs': ['adult_dc2.dc']},
  
]

dc_detector = DuckDCDetector()

for config in configs:
  dataset_file = f'{ROOT_PATH}/original_datasets/' + config['dataset']
  output_file = f'{ROOT_PATH}/clean_datasets/' + config['dataset']
  
  df = pandas.read_csv(dataset_file)

  for dc_address in config['dcs']:
    dc_file_address = f'{ROOT_PATH}/dcs/{dc_address}'
    dc_reader = DCReader(dc_file_address)
    df = DatasetOps.clean_dataset(df, dc_reader, dc_detector)
    
    is_clean = DatasetOps.is_clean_dataset(df, dc_reader, dc_detector)
    print(f"{config['dataset']}:\t", "CLEAN" if is_clean else "NOISY", f"\t\t{dc_address}")
    
  df.to_csv(output_file, index=False) # type: ignore
  
    
    
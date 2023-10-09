import time, pandas
from dcd.core.dc_reader import DCReader
from dcd.duck.dc_detector import DCDetector as DuckDCDetector

from dcd.tools.dataset_operations import DatasetOps

# from config.count_violations_config import DC_FILE, DATASET_FILE

def count_violations(dataset_file, dc_file):
  print(f"Checking:\t\t {dataset_file}")
  print(f"Applying:\t\t {dc_file}")
  print()
  dc = DCReader(dc_file).pop_dc()

  df = pandas.read_csv(dataset_file)

  vio_qtd = DatasetOps.count_violations(df, dc)
  tuples_on_violations = DatasetOps.tuples_on_violations(df, dc)

  print("Violations:\t\t", vio_qtd)
  print("Tuples on violations:\t", len(tuples_on_violations))
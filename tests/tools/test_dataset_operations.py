import unittest
import pandas as pd
from dcd.core.dc_reader import DCReader

from dcd.tools.dataset_operations import DatasetOps

DC_FILE = 'testdatas/dcs/flights_dc2.txt'
DATASET_FILE = './flights_noisy_0.1.csv'
NOISY_PERCENTAGE = 0.1

class TestDatasetOps(unittest.TestCase):
  
  def test_datasetops_methods(self):
    dc = DCReader(DC_FILE).pop_dc()
    df = pd.read_csv(DATASET_FILE)
    
    vio_qtd = DatasetOps.count_violations(df.copy(), dc)
    
    self.assertEqual(vio_qtd, 16, "Incorrect number of violations detected, must be 16")
    
  def test_datasetops_tuples_on_violations(self):
    dc = DCReader(DC_FILE).pop_dc()
    df = pd.read_csv(DATASET_FILE)
    
    tuples_on_violations = DatasetOps.tuples_on_violations(df.copy(), dc)
    tuples_qtd = len(tuples_on_violations)
    
    self.assertEqual(tuples_qtd, 18, "Incorrect number of tuples on violations, must be 18")
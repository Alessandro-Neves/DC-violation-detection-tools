import pandas as pd

from dcd.tools.dataset_operations import DatasetOps
from dcd.core.dc_reader import DCReader
from dcd.types.predicate import PREDICATE_OPERATOR
import random

from config.gen_noisy_config import DC_FILE, DATASET_FILE, NOISY_PERCENTAGE

WITH_EQUALITY_OPERATORS = [
  PREDICATE_OPERATOR.EQ,
  PREDICATE_OPERATOR.GTE,
  PREDICATE_OPERATOR.LTE
]

dc = DCReader(DC_FILE).pop_dc()

df = pd.read_csv(DATASET_FILE)
dfc = df.copy()

num_tuples = df.shape[0]

desired_noisy_qtd = int(num_tuples * (NOISY_PERCENTAGE / 100))

NOISY_RANGE_ERROR = (desired_noisy_qtd * 0.05)

num_violations = 0

print("Generating DC violations: ", desired_noisy_qtd)

iterations = 0

for it in range(desired_noisy_qtd * 10):
  iterations = it
  if (num_violations > desired_noisy_qtd - NOISY_RANGE_ERROR):
    break
  
  idx1 = random.randint(0, num_tuples - 1)
  idx2 = random.randint(0, num_tuples - 1)
  
  dft = novo_df = df.copy().loc[[idx1, idx2]]
  
  vio_qtd = DatasetOps.count_violations(dft, dc)
  
  if vio_qtd == 0:
    predicates = dc.get_predicates()
    for predicate in predicates:
      col_name_A = predicate.left_side.col_name_or_value
      col_name_B = predicate.right_side.col_name_or_value
    
      # If 𝜌 ∈ {=, ≤, ≥}, change t[𝐴] -> t[𝐵]
      if predicate.operator in WITH_EQUALITY_OPERATORS:
        dfc.at[idx1, col_name_A] = dfc.at[idx2, col_name_B]
      # If 𝜌 ∈ {<, >, ≠}, change t[A] to another value from the active domain of the attribute such that 𝑃 is satisfied
      else: 
        if not predicate.operator == PREDICATE_OPERATOR.IQ:
          continue
          
        new_value = dfc.at[idx2, col_name_B] + 1 if predicate.operator == PREDICATE_OPERATOR.GT else -1
        dfc.at[idx1, col_name_A] = new_value
        
        print(col_name_A, new_value, col_name_B, vio_qtd_dfc)
  
      vio_qtd_dfc = len(DatasetOps.tuples_on_violations(dfc, dc))
      
      # print(vio_qtd_dfc)
      
      if vio_qtd_dfc > num_violations and vio_qtd_dfc < (desired_noisy_qtd + NOISY_RANGE_ERROR):
        df = dfc.copy()
        print(f"{vio_qtd_dfc}/{desired_noisy_qtd}")
        num_violations = vio_qtd_dfc
      else:
        dfc = df.copy()

print("Iterations: ", iterations)
print("Violations: ",DatasetOps.count_violations(df, dc))
print("Tuples on some violation: ", len(DatasetOps.tuples_on_violations(df, dc)))

df.to_csv(f'tax_100k_noisy_{NOISY_PERCENTAGE}.csv', index=False) # type: ignore



[(1448, 1871), (1660, 1871), (3813, 1871), (4133, 1871), (4165, 1871), (4427, 1871), (9151, 1871), (10954, 1871), (11751, 1871), (12538, 1871), (12893, 1871), (16240, 17625), (16240, 4820), (16240, 4505), (16240, 1058), (17288, 1871)]

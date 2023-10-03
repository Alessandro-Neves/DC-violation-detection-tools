import unittest



from dcd.core.dc_reader import DCReader
dc = DCReader(DC_FILE).pop_dc()



class TestDCReader(unittest.TestCase):
  
  def test_if_read_dc_file_correctly(self):
    self.assertTrue(True)
    
  def test_if_read_dc_file_correctly_X(self):
    self.assertTrue(True)
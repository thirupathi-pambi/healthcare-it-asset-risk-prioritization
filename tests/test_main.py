import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from main import score
class AssetTests(unittest.TestCase):
 def test_risk(self):self.assertEqual(score({'condition':'critical','type':'workstation','os':'Windows 10','purchase_year':'2020'}),100)
 def test_healthy(self):self.assertEqual(score({'condition':'healthy','type':'switch','os':'n/a','purchase_year':'2025'}),0)

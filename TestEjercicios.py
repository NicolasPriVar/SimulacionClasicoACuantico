import DeLoClasicoALoCuantico as cc
import unittest
import numpy as np

class Testejercicios(unittest.TestCase):
    def test_canicas(self):
        #Primer caso de prueba (con 4 clicks)
        v1=cc.multi([[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,0,0,0,1],[0,0,0,1,0,0],[0,0,1,0,0,0],[1,0,0,0,1,0]], [6,2,1,5,3,10], 4)
        self.assertAlmostEqual(v1, [0, 0, 12, 5, 1, 9])
        #Segundo caso de prueba (con 2 clicks)
        v1=cc.multi([[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,0,0,0,1],[0,0,0,1,0,0],[0,0,1,0,0,0],[1,0,0,0,1,0]], [6,2,1,5,3,10], 2)
        self.assertAlmostEqual(v1, [0, 0, 9, 5, 12, 1])
    def test_rendijas(self):
        #Primer caso de prueba (con 1 click)
        v1=cc.rendijas([[0,0,0,0,0,0,0,0],[1/2,0,0,0,0,0,0,0],[1/2,0,0,0,0,0,0,0],[0,1/3,0,1,0,0,0,0],[0,1/3,0,0,1,0,0,0],[0,1/3,1/3,0,0,1,0,0],[0,0,1/3,0,0,0,1,0],[0,0,1/3,0,0,0,0,1]],[1,0,0,0,0,0,0,0],1)
        self.assertAlmostEqual(v1, [0.0, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0])
        #Segundo caso de preba (con 2 clicks)
        v1=cc.rendijas([[0,0,0,0,0,0,0,0],[1/2,0,0,0,0,0,0,0],[1/2,0,0,0,0,0,0,0],[0,1/3,0,1,0,0,0,0],[0,1/3,0,0,1,0,0,0],[0,1/3,1/3,0,0,1,0,0],[0,0,1/3,0,0,0,1,0],[0,0,1/3,0,0,0,0,1]], [1,0,0,0,0,0,0,0], 2)
        self.assertAlmostEqual(v1, [0.0, 0.0, 0.0, 0.16666666666666666, 0.16666666666666666, 0.3333333333333333, 0.16666666666666666, 0.16666666666666666])
    def test_cuantico(self):
        #Primer caso de prueba (con 2 clciks)
        v1=cc.scuantico([[0,1/np.sqrt(2),1/np.sqrt(2),0], [1/np.sqrt(2),0,0,-(1/np.sqrt(2))],[1/np.sqrt(2),0,0,1/np.sqrt(2)],[0,-(1/np.sqrt(2)),1/np.sqrt(2),0]], [1,0,0,0], 2)
        self.assertAlmostEqual(v1, [0.9999999999999998, 0.0, 0.0, 0.9999999999999998])
        #Segundo caso de prueba (con 1 clciks)
        v1=cc.scuantico([[0,1/np.sqrt(2),1/np.sqrt(2),0], [1/np.sqrt(2),0,0,-(1/np.sqrt(2))],[1/np.sqrt(2),0,0,1/np.sqrt(2)],[0,-(1/np.sqrt(2)),1/np.sqrt(2),0]], [1,0,0,0], 1)
        self.assertAlmostEqual(v1, [0.0, 0.7071067811865475, 0.7071067811865475, 0.0])
if __name__ == '__main__':
    unittest.main()
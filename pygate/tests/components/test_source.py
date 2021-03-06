import unittest
from pygate.components.source import *
from pygate.utils.strs import assert_equal_ignoring_multiple_whitespaces as ae


class TestParticlePositron(unittest.TestCase):
    def test_render(self):
        p = ParticlePositron()
        src = Source('src', particle=p)
        self.assertEqual(p.render(),
                         '/gate/source/src/gps/particle e+ \n/gate/source/src/gps/energytype Fluor18\n/gate/source/src/setForcedUnstableFlag true\n/gate/source/src/setForcedHalfLife 6586 s\n')


class TestParticleGamma(unittest.TestCase):
    def test_render(self):
        p = ParticleGamma()
        src = Source('src', particle=p)
        self.assertEqual(p.render(),
                         '/gate/source/src/gps/particle gamma \n/gate/source/src/setType backtoback\n/gate/source/src/gps/monoenergy 511 keV\n/gate/source/src/setForcedUnstableFlag true\n/gate/source/src/setForcedHalfLife 6586.2 s\n')


class TestAngularISO(unittest.TestCase):
    def test_render(self):
        a = AngularISO()
        src = Source('src', angle=a)
        self.assertEqual(a.render(),
                         '/gate/source/src/gps/angtype iso\n/gate/source/src/gps/mintheta 0 deg \n/gate/source/src/gps/maxtheta 180 deg\n/gate/source/src/gps/minphi   0 deg\n/gate/source/src/gps/maxphi   360 deg\n')


class TestVoxelized(unittest.TestCase):
    def test_render(self):
        v = Voxelized('act_range.dat', 'act.h33',
                      position=Vec3(-128.0, -128.0, -0.15))
        src = Source('src', shape=v)
        self.assertEqual(v.render(),
                         '/gate/source/src/reader/insert interfile\n/gate/source/src/interfileReader/translator/insert range \n/gate/source/src/interfileReader/rangeTranslator/readTable act_range.dat\n/gate/source/src/interfileReader/readFile  act.h33\n')


class TestCylinder(unittest.TestCase):
    def test_render(self):
        c = Cylinder(10.0, 10.0, 'Surface')
        src = Source('src', shape=c)
        self.assertEqual(c.render(),
                         '/gate/source/src/gps/type Surface\n/gate/source/src/gps/shape Cylinder\n/gate/source/src/gps/radius 10.0 mm\n/gate/source/src/gps/halfz 10.0 mm\n')


class TestSphere(unittest.TestCase):
    def test_render(self):
        s = Sphere(10.0, 'Surface')
        src = Source('src', shape=s)
        ae(self, s.render(),
           '/gate/source/src/gps/type Surface\n/gate/source/src/gps/shape Sphere\n/gate/source/src/gps/radius 10.0 mm\n')


class TestSource(unittest.TestCase):
    def test_render_voxel(self):
        p = ParticleGamma()
        ang = AngularISO()
        v = Voxelized('act_range.dat', 'act.h33',
                      position=Vec3(-128.0, -128.0, -0.15))
        src = Source('src', p, angle=ang, shape=v)
        self.assertEqual(src.render(),
                         '/gate/source/addSource src voxel\n/gate/source/src/reader/insert interfile\n/gate/source/src/interfileReader/translator/insert range \n/gate/source/src/interfileReader/rangeTranslator/readTable act_range.dat\n/gate/source/src/interfileReader/readFile  act.h33\n\n/gate/source/src/gps/particle gamma \n/gate/source/src/setType backtoback\n/gate/source/src/gps/monoenergy 511 keV\n/gate/source/src/setForcedUnstableFlag true\n/gate/source/src/setForcedHalfLife 6586.2 s\n\n/gate/source/src/gps/angtype iso\n/gate/source/src/gps/mintheta 0 deg \n/gate/source/src/gps/maxtheta 180 deg\n/gate/source/src/gps/minphi   0 deg\n/gate/source/src/gps/maxphi   360 deg\n\n')

    def test_render_cylindrical_pet_wiki(self):
        p = ParticleGamma(halflife=1223,)
        a = AngularISO()
        src = Source('posiC11', p, 10000, a)
        ae(self, src.render(),
           '/gate/source/addSource posiC11\n/gate/source/posiC11/gps/particle gamma \n/gate/source/posiC11/setType backtoback\n/gate/source/posiC11/gps/monoenergy 511 keV\n/gate/source/posiC11/setForcedUnstableFlag true\n/gate/source/posiC11/setForcedHalfLife 1223 s\n/gate/source/posiC11/setActivity 10000 becquerel\n/gate/source/posiC11/gps/angtype iso\n/gate/source/posiC11/gps/mintheta 0 deg \n/gate/source/posiC11/gps/maxtheta 180 deg\n/gate/source/posiC11/gps/minphi   0 deg\n/gate/source/posiC11/gps/maxphi   360 deg\n\n')

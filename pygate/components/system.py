from .base import ObjectWithTemplate


class System(ObjectWithTemplate):
    template = 'geometry/system'
    name = None
    attach_systems = None

    def __init__(self, sensitive_detectors=None):
        self.levels = self.attach_systems()
        self.levels = {k: self.levels[k]
                       for k in self.levels if self.levels[k] is not None}
        if sensitive_detectors is None:
            sensitive_detectors = tuple()
        self.sds = sensitive_detectors


class PETscanner(System):
    name = 'PETscanner'

    def __init__(self, level1, level2, level3, level4, level5, sensitive_detectors=None):
        self.attach_systems = lambda: {
            'level1': level1,
            'level2': level2,
            'level3': level3,
            'level4': level4,
            'level5': level5
        }
        super().__init__(sensitive_detectors)


class Ecat(System):
    name = 'ecat'

    def __init__(self, block=None, crystal=None, sensitive_detectors=None):
        self.attach_systems = lambda:  {'block': block, 'crystal': crystal}
        super().__init__(sensitive_detectors)


class CylindericalPET(System):
    name = 'cylindricalPET'

    def __init__(self,
                 rsector=None, module=None, submodule=None, crystal=None,
                 layer0=None, layer1=None, layer2=None, layer3=None,
                 sensitive_detectors=None):
        self.attach_systems = lambda: {
            'rsector': rsector,
            'module': module,
            'submodule': submodule,
            'crystal': crystal,
            'layer0': layer0,
            'layer1': layer1,
            'layer2': layer2,
            'layer3': layer3,
        }
        super().__init__(sensitive_detectors)

class MultiPatchPET(System):
    name = 'multiPatchPET'
    def __init__(self, container, patch_list, sensitive_detectors = None):
        self.attach_systems = lambda: {'contianer':container, 
        'patch_list':patch_list}
        super().__init__(sensitive_detectors)

class SPECThead(System):
    name = 'SPECThead'
    def __init__(self, crystal, pixel = None, sensitive_detectors = None):
        self.attach_systems = lambda: {'crystal': crystal, 'pixel':pixel }
        super().__init__(sensitive_detectors)

class OpticalSystem(System):
    name = 'OpticalSystem'
    def __init__(self,crystal, pixel = None, sensitive_detectors = None):
        self.attach_systems = lambda: {'crystal': crystal, 'pixel':pixel}
        super().__init__(sensitive_detectors)

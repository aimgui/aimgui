from .fixed_control import FixedControl
from .dynamic_control import DynamicControl
from .output_range import OutputRange
from .building_lfo import BuildingLfo
from .math_ops import MathOps
from .multichannel_expansion import MultichannelExpansion
from .multichannel_expansion_2 import MultichannelExpansion2
from .handling_channels import HandlingChannels
from .handling_channels_2 import HandlingChannels2
from .handling_channels_3 import HandlingChannels3
from .handling_channels_4 import HandlingChannels4

def install(app):
    app.add_page(FixedControl, "controls")
    app.add_page(DynamicControl, "controls")
    app.add_page(OutputRange, "controls")
    app.add_page(BuildingLfo, "controls")
    app.add_page(MathOps, "controls")
    app.add_page(MultichannelExpansion, "controls")
    app.add_page(MultichannelExpansion2, "controls")
    app.add_page(HandlingChannels, "controls")
    app.add_page(HandlingChannels2, "controls")
    app.add_page(HandlingChannels3, "controls")
    app.add_page(HandlingChannels4, "controls")

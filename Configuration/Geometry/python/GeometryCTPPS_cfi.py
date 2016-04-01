import FWCore.ParameterSet.Config as cms

# DDL geometry (ideal)
XMLIdealGeometryESSource = cms.ESSource("XMLIdealGeometryESSource",
    geomXMLFiles = cms.vstring('Geometry/CMSCommonData/data/materials.xml', 
        'Geometry/CMSCommonData/data/rotations.xml', 
        'Geometry/CMSCommonData/data/extend/cmsextent.xml', 
        'Geometry/CMSCommonData/data/cms.xml', 
        'Geometry/CMSCommonData/data/PhaseI/beampipe.xml', 
        'Geometry/CMSCommonData/data/cmsBeam.xml', 
        'Geometry/CMSCommonData/data/cmsMother.xml', 
        'Geometry/CMSCommonData/data/mgnt.xml', 
        'Geometry/ForwardCommonData/data/forward.xml', 
        'Geometry/ForwardCommonData/data/totemRotations.xml', 
        'Geometry/ForwardCommonData/data/totemMaterials.xml', 
        'Geometry/ForwardCommonData/data/totemt1.xml', 
        'Geometry/ForwardCommonData/data/totemt2.xml', 
        'Geometry/ForwardCommonData/data/ionpump.xml', 
        'Geometry/CTPPSCommonData/data/CTPPS_Box.xml',
        'Geometry/CTPPSCommonData/data/CTPPS_Box/CTPPS_Box_002.xml',
        'Geometry/CTPPSCommonData/data/CTPPS_Box/CTPPS_Box_003.xml',
        'Geometry/CTPPSCommonData/data/CTPPS_Box/CTPPS_Box_102.xml',
        'Geometry/CTPPSCommonData/data/CTPPS_Box/CTPPS_Box_103.xml',
        'Geometry/CTPPSCommonData/data/CTPPS_Hybrid.xml', 
        'Geometry/CTPPSCommonData/data/CTPPS_Materials.xml', 
        'Geometry/CTPPSCommonData/data/CTPPS_Transformations.xml', 
        'Geometry/CTPPSCommonData/data/CTPPS_Tracker_Assembly_Box_Real_002.xml',
        'Geometry/CTPPSCommonData/data/CTPPS_Tracker_Assembly_Box_Real_003.xml',
        'Geometry/CTPPSCommonData/data/CTPPS_Tracker_Assembly_Box_Real_102.xml',
        'Geometry/CTPPSCommonData/data/CTPPS_Tracker_Assembly_Box_Real_103.xml',
        'Geometry/CTPPSCommonData/data/CTPPS_Device.xml', 
        'Geometry/CTPPSCommonData/data/CTPPS_Horizontal_Device.xml',
        'Geometry/CTPPSCommonData/data/CTPPS_FirstTr_1_Station.xml', 
        'Geometry/CTPPSCommonData/data/CTPPS_FirstTr_2_Station.xml', 
        'Geometry/CTPPSCommonData/data/CTPPS_SecondTr_1_Station.xml', 
        'Geometry/CTPPSCommonData/data/CTPPS_SecondTr_2_Station.xml', 
        'Geometry/CTPPSCommonData/data/CTPPS_Tracker_Materials.xml',#FF
        'Geometry/CTPPSCommonData/data/CTPPS_Tracker_Module.xml',#FF
        'Geometry/CTPPSCommonData/data/CTPPS_Tracker_Sensitive_Dets.xml',#FF
        'Geometry/CTPPSCommonData/data/CTPPS_Timing_Materials.xml',#SM
        'Geometry/CTPPSCommonData/data/CTPPS_Timing_Transformations.xml',#SM
        'Geometry/CTPPSCommonData/data/CTPPS_Timing_Horizontal_Pot.xml',#SM
        'Geometry/CTPPSCommonData/data/CTPPS_Timing_Lbar.xml',#SM
        'Geometry/CTPPSCommonData/data/CTPPS_Timing_Lbars/CTPPS_Timing_Lbar_A13.xml',#SM
        'Geometry/CTPPSCommonData/data/CTPPS_Timing_Lbars/CTPPS_Timing_Lbar_A24.xml',#SM
        'Geometry/CTPPSCommonData/data/CTPPS_Timing_Lbars/CTPPS_Timing_Lbar_B13.xml',#SM
        'Geometry/CTPPSCommonData/data/CTPPS_Timing_Lbars/CTPPS_Timing_Lbar_B24.xml',#SM
        'Geometry/CTPPSCommonData/data/CTPPS_Timing_Lbars/CTPPS_Timing_Lbar_C13.xml',#SM
        'Geometry/CTPPSCommonData/data/CTPPS_Timing_Lbars/CTPPS_Timing_Lbar_C24.xml',#SM
        'Geometry/CTPPSCommonData/data/CTPPS_Timing_Lbars/CTPPS_Timing_Lbar_D13.xml',#SM
        'Geometry/CTPPSCommonData/data/CTPPS_Timing_Lbars/CTPPS_Timing_Lbar_D24.xml',#SM
        'Geometry/CTPPSCommonData/data/CTPPS_Timing_Lbars/CTPPS_Timing_Lbar_E13.xml',#SM
        'Geometry/CTPPSCommonData/data/CTPPS_Timing_Lbars/CTPPS_Timing_Lbar_E24.xml',#SM
        'Geometry/CTPPSCommonData/data/CTPPS_Timing_Box_1.xml',
        'Geometry/CTPPSCommonData/data/CTPPS_Timing_Box_2.xml',
        'Geometry/CTPPSCommonData/data/CTPPS_Timing_1_Detector_Assembly.xml',#SM
        'Geometry/CTPPSCommonData/data/CTPPS_Timing_2_Detector_Assembly.xml',#SM
        'Geometry/CTPPSCommonData/data/CTPPS_Timing_1_Station.xml', 
        'Geometry/CTPPSCommonData/data/CTPPS_Timing_2_Station.xml', 
        'Geometry/CTPPSCommonData/data/CTPPS_Stations_Assembly.xml', 
        'Geometry/CTPPSCommonData/data/CTPPS_Timing_Sensitive_Dets.xml', 
        'Geometry/CTPPSCommonData/data/CTPPS_Sensitive_Dets.xml', 
        'Geometry/CTPPSCommonData/data/CTPPS_Cuts_Per_Region.xml', 
        'Geometry/CTPPSCommonData/data/CTPPS_Global.xml'), 
     rootNodeName = cms.string('cms:OCMS')
)

# extended geometries
TotemRPGeometryESModule = cms.ESProducer("TotemRPGeometryESModule")

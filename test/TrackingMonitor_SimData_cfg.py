# The following comments couldn't be translated into the new config version:

#--------------------------
# DQMServices
#--------------------------

import FWCore.ParameterSet.Config as cms

process = cms.Process("DQMOnlineSimData")
#-------------------------------------------------
# MAGNETIC FIELD
#-------------------------------------------------
process.load("Configuration.StandardSequences.MagneticField_cff")

#--------------------------
# Tracking Monitor
#--------------------------
process.load("DQM.TrackingMonitor.TrackingMonitor_cfi")

process.MessageLogger = cms.Service("MessageLogger",
    debugModules = cms.untracked.vstring('TrackMon'),
    cout = cms.untracked.PSet(
        threshold = cms.untracked.string('INFO')
    ),
    destinations = cms.untracked.vstring('cout')
)

process.DQMStore = cms.Service("DQMStore",
    referenceFileName = cms.untracked.string(''),
    verbose = cms.untracked.int32(0)
)

process.outP = cms.OutputModule("AsciiOutputModule")

process.AdaptorConfig = cms.Service("AdaptorConfig")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/relval/2008/7/21/RelVal-RelValQCD_Pt_80_120-1216579576-STARTUP_V4-2nd/RelValQCD_Pt_80_120/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/CMSSW_2_1_0_pre9-RelVal-1216579576-STARTUP_V4-2nd-unmerged/0000/0A81C8A7-6E57-DD11-8B07-00161757BF42.root', 
        '/store/relval/2008/7/21/RelVal-RelValQCD_Pt_80_120-1216579576-STARTUP_V4-2nd/RelValQCD_Pt_80_120/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/CMSSW_2_1_0_pre9-RelVal-1216579576-STARTUP_V4-2nd-unmerged/0000/0CDA198B-7057-DD11-B23E-001617C3B77C.root', 
        '/store/relval/2008/7/21/RelVal-RelValQCD_Pt_80_120-1216579576-STARTUP_V4-2nd/RelValQCD_Pt_80_120/GEN-SIM-DIGI-RAW-HLTDEBUG-RECO/CMSSW_2_1_0_pre9-RelVal-1216579576-STARTUP_V4-2nd-unmerged/0000/182EA0C2-7057-DD11-9B09-000423D9880C.root')
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(200)
)
process.p = cms.Path(process.TrackMon)
process.ep = cms.EndPath(process.outP)
process.TrackMon.OutputMEsInRootFile = True


#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Tests for fastatoflat.py

"""

__author__ = 'Chris Lasher'
__email__ = 'chris DOT lasher <AT> gmail DOT com'

import Bio.SeqIO
import os
import StringIO
import sys
import unittest

parpath = os.path.join(os.path.dirname(sys.argv[0]), os.pardir)
sys.path.insert(0, os.path.abspath(parpath))
import fastatoflat


class FastaToFlatTests(unittest.TestCase):
    """
    Tests for fastatoflat.

    """

    records_and_expected = [
        (
            """\
>gi|114052567|ref|NP_001039362.1| NGFI-A binding protein 2 [Bos taurus]
MHRAASPTAEQPPGGGDSARRTPQPRLKPSSRAMALPRTLGELQLYRVLQRANLLSYYETFIQQGGDDVQ
QLCEAGEEEFLEIMALVGMATKPLHVRRLQKALREWATNPGLFSQPVPAVPVSSIPLFKISETAGTRKGS
MSNGHGSPGEKAGSARSFSPKSPLELGEKLSPLPGGPGAGDPRIWPGRSTPESDVGAGGEEEAGSPPFSP
PAGGGGPEGTGAGGLAAAGTGGGPDRLEPEMVRMVVESVERIFRSFPRGDAGEVTSLLKLNKKLARSVGH
IFEMDDNDSQKEEEIRKYSIIYGRFDSKRREGKQLSLHELTINEAAAQFCMRDNTLLLRRVELFSLSRQV
ARESTYLSSLKGSRLHPEELGGPPLKKLKQEVGEQSHSEIQQPPPGPESYAPPFRPSLEEDSASLSGESL
DGHLQAVGSCPRLTPPPADLPLALPAHGLWSRHILQQTLMDEGLRLARLVSHDRVGRLSPCVPAKPPLAE
FEEGLLDRCPAPGPHPALVEGRRNSVKVEAEASRQ
""",
            {
                'gi': '114052567',
                'accession': 'NP_001039362.1',
                'genus_species': 'Bos taurus',
                'annotation': 'NGFI-A binding protein 2 [Bos taurus]',
                'sequence': 'MHRAASPTAEQPPGGGDSARRTPQPRLKPSSRAMALPRTLGELQLYRVLQRANLLSYYETFIQQGGDDVQQLCEAGEEEFLEIMALVGMATKPLHVRRLQKALREWATNPGLFSQPVPAVPVSSIPLFKISETAGTRKGSMSNGHGSPGEKAGSARSFSPKSPLELGEKLSPLPGGPGAGDPRIWPGRSTPESDVGAGGEEEAGSPPFSPPAGGGGPEGTGAGGLAAAGTGGGPDRLEPEMVRMVVESVERIFRSFPRGDAGEVTSLLKLNKKLARSVGHIFEMDDNDSQKEEEIRKYSIIYGRFDSKRREGKQLSLHELTINEAAAQFCMRDNTLLLRRVELFSLSRQVARESTYLSSLKGSRLHPEELGGPPLKKLKQEVGEQSHSEIQQPPPGPESYAPPFRPSLEEDSASLSGESLDGHLQAVGSCPRLTPPPADLPLALPAHGLWSRHILQQTLMDEGLRLARLVSHDRVGRLSPCVPAKPPLAEFEEGLLDRCPAPGPHPALVEGRRNSVKVEAEASRQ'
            },
            '114052567\tNP_001039362.1\tBos taurus\tNGFI-A binding protein 2 [Bos taurus]\tMHRAASPTAEQPPGGGDSARRTPQPRLKPSSRAMALPRTLGELQLYRVLQRANLLSYYETFIQQGGDDVQQLCEAGEEEFLEIMALVGMATKPLHVRRLQKALREWATNPGLFSQPVPAVPVSSIPLFKISETAGTRKGSMSNGHGSPGEKAGSARSFSPKSPLELGEKLSPLPGGPGAGDPRIWPGRSTPESDVGAGGEEEAGSPPFSPPAGGGGPEGTGAGGLAAAGTGGGPDRLEPEMVRMVVESVERIFRSFPRGDAGEVTSLLKLNKKLARSVGHIFEMDDNDSQKEEEIRKYSIIYGRFDSKRREGKQLSLHELTINEAAAQFCMRDNTLLLRRVELFSLSRQVARESTYLSSLKGSRLHPEELGGPPLKKLKQEVGEQSHSEIQQPPPGPESYAPPFRPSLEEDSASLSGESLDGHLQAVGSCPRLTPPPADLPLALPAHGLWSRHILQQTLMDEGLRLARLVSHDRVGRLSPCVPAKPPLAEFEEGLLDRCPAPGPHPALVEGRRNSVKVEAEASRQ'
        ),
        (
            """\
>gi|11466083|ref|NP_041730.1| hypothetical protein [Neurospora crassa]
MESGIPQDISEYLTVLNRSLVVLTSEDKIPEPHRDVIFNSDGTPNPNLPKDVQGRILKDPDFVEILRRRG
FTDIATNGVPQGASTSCGLATYNVKELFKRYDELIMYADDGILCRQDPSTPDFSVEEAGVVQEPAKSGWI
KQNGEFKKSVKFLGLEFIPANIPPLGEGEVKDYPRLRGATRNGSKMELSTELQFLCYLSYKLRIKVLRDL
YIQVLGYLPSVPLLRYRSLAEAINELSPKRITIGQFITSSFEEFTA
""",
            {
                'gi': '11466083',
                'accession': 'NP_041730.1',
                'genus_species': 'Neurospora crassa',
                'annotation': 'hypothetical protein [Neurospora crassa]',
                'sequence': 'MESGIPQDISEYLTVLNRSLVVLTSEDKIPEPHRDVIFNSDGTPNPNLPKDVQGRILKDPDFVEILRRRGFTDIATNGVPQGASTSCGLATYNVKELFKRYDELIMYADDGILCRQDPSTPDFSVEEAGVVQEPAKSGWIKQNGEFKKSVKFLGLEFIPANIPPLGEGEVKDYPRLRGATRNGSKMELSTELQFLCYLSYKLRIKVLRDLYIQVLGYLPSVPLLRYRSLAEAINELSPKRITIGQFITSSFEEFTA'
            },
            '11466083\tNP_041730.1\tNeurospora crassa\thypothetical protein [Neurospora crassa]\tMESGIPQDISEYLTVLNRSLVVLTSEDKIPEPHRDVIFNSDGTPNPNLPKDVQGRILKDPDFVEILRRRGFTDIATNGVPQGASTSCGLATYNVKELFKRYDELIMYADDGILCRQDPSTPDFSVEEAGVVQEPAKSGWIKQNGEFKKSVKFLGLEFIPANIPPLGEGEVKDYPRLRGATRNGSKMELSTELQFLCYLSYKLRIKVLRDLYIQVLGYLPSVPLLRYRSLAEAINELSPKRITIGQFITSSFEEFTA'
        ),
        (
            """\
>gi|221229395|ref|YP_002502811.1| superoxide dismutase [Mycobacterium leprae Br4923]
MAEYTLPDLDWDYAALEPHISGEINEIHHTKHHAAYVKGVNDALAKLDEARAKDDHSAIFLNEKNLAFHL
GGHVNHSIWWKNLSPNGGDKPTGGLATDIDETFGSFDKFRAQFSAAANGLQGSGWAVLGYDTLGNKLLTF
QLYDQQANVSLGIIPLLQVDMWEHAFYLQYKNVKADYVKAFWNVVNWADVQSRYMAATSKTQGLIFD
""",
            {
                'gi': '221229395',
                'accession': 'YP_002502811.1',
                'genus_species': 'Mycobacterium leprae Br4923',
                'annotation': 'superoxide dismutase [Mycobacterium leprae Br4923]',
                'sequence': 'MAEYTLPDLDWDYAALEPHISGEINEIHHTKHHAAYVKGVNDALAKLDEARAKDDHSAIFLNEKNLAFHLGGHVNHSIWWKNLSPNGGDKPTGGLATDIDETFGSFDKFRAQFSAAANGLQGSGWAVLGYDTLGNKLLTFQLYDQQANVSLGIIPLLQVDMWEHAFYLQYKNVKADYVKAFWNVVNWADVQSRYMAATSKTQGLIFD'
            },
            '221229395\tYP_002502811.1\tMycobacterium leprae Br4923\tsuperoxide dismutase [Mycobacterium leprae Br4923]\tMAEYTLPDLDWDYAALEPHISGEINEIHHTKHHAAYVKGVNDALAKLDEARAKDDHSAIFLNEKNLAFHLGGHVNHSIWWKNLSPNGGDKPTGGLATDIDETFGSFDKFRAQFSAAANGLQGSGWAVLGYDTLGNKLLTFQLYDQQANVSLGIIPLLQVDMWEHAFYLQYKNVKADYVKAFWNVVNWADVQSRYMAATSKTQGLIFD'
        ),
        (
            """\
>gi|30678651|ref|NP_191957.2| ATMYC1 (Arabidopsis thaliana myc-related transcription factor 1); DNA binding / transcription factor
MSLTMADGVEAAAGRSKRQNSLLRKQLALAVRSVQWSYAIFWSSSLTQPGVLEWGEGCYNGDMKKRKKSY
ESHYKYGLQKSKELRKLYLSMLEGDSGTTVSTTHDNLNDDDDNCHSTSMMLSPDDLSDEEWYYLVSMSYV
FSPSQCLPGRASATGETIWLCNAQYAENKLFSRSLLARSASIQTVVCFPYLGGVIELGVTELISEDHNLL
RNIKSCLMEISAHQDNDDEKKMEIKISEEKHQLPLGISDEDLHYKRTISTVLNYSADRSGKNDKNIRHRQ
PNIVTSEPGSSFLRWKQCEQQVSGFVQKKKSQNVLRKILHDVPLMHTKRMFPSQNSGLNQDDPSDRRKEN
EKFSVLRTMVPTVNEVDKESILNNTIKYLQELEARVEELESCMGSVNFVERQRKTTENLNDSVLIEETSG
NYDDSTKIDDNSGETEQVTVFRDKTHLRVKLKETEVVIEVRCSYRDYIVADIMETLSNLHMDAFSVRSHT
LNKFLTLNLKAKFRGAAVASVGMIKRELRRVIGDLF
""",
            {
                'gi': '30678651',
                'accession': 'NP_191957.2',
                'genus_species': '',
                'annotation': 'ATMYC1 (Arabidopsis thaliana myc-related transcription factor 1); DNA binding / transcription factor',
                'sequence': 'MSLTMADGVEAAAGRSKRQNSLLRKQLALAVRSVQWSYAIFWSSSLTQPGVLEWGEGCYNGDMKKRKKSYESHYKYGLQKSKELRKLYLSMLEGDSGTTVSTTHDNLNDDDDNCHSTSMMLSPDDLSDEEWYYLVSMSYVFSPSQCLPGRASATGETIWLCNAQYAENKLFSRSLLARSASIQTVVCFPYLGGVIELGVTELISEDHNLLRNIKSCLMEISAHQDNDDEKKMEIKISEEKHQLPLGISDEDLHYKRTISTVLNYSADRSGKNDKNIRHRQPNIVTSEPGSSFLRWKQCEQQVSGFVQKKKSQNVLRKILHDVPLMHTKRMFPSQNSGLNQDDPSDRRKENEKFSVLRTMVPTVNEVDKESILNNTIKYLQELEARVEELESCMGSVNFVERQRKTTENLNDSVLIEETSGNYDDSTKIDDNSGETEQVTVFRDKTHLRVKLKETEVVIEVRCSYRDYIVADIMETLSNLHMDAFSVRSHTLNKFLTLNLKAKFRGAAVASVGMIKRELRRVIGDLF'
            },
            '30678651\tNP_191957.2\t\tATMYC1 (Arabidopsis thaliana myc-related transcription factor 1); DNA binding / transcription factor\tMSLTMADGVEAAAGRSKRQNSLLRKQLALAVRSVQWSYAIFWSSSLTQPGVLEWGEGCYNGDMKKRKKSYESHYKYGLQKSKELRKLYLSMLEGDSGTTVSTTHDNLNDDDDNCHSTSMMLSPDDLSDEEWYYLVSMSYVFSPSQCLPGRASATGETIWLCNAQYAENKLFSRSLLARSASIQTVVCFPYLGGVIELGVTELISEDHNLLRNIKSCLMEISAHQDNDDEKKMEIKISEEKHQLPLGISDEDLHYKRTISTVLNYSADRSGKNDKNIRHRQPNIVTSEPGSSFLRWKQCEQQVSGFVQKKKSQNVLRKILHDVPLMHTKRMFPSQNSGLNQDDPSDRRKENEKFSVLRTMVPTVNEVDKESILNNTIKYLQELEARVEELESCMGSVNFVERQRKTTENLNDSVLIEETSGNYDDSTKIDDNSGETEQVTVFRDKTHLRVKLKETEVVIEVRCSYRDYIVADIMETLSNLHMDAFSVRSHTLNKFLTLNLKAKFRGAAVASVGMIKRELRRVIGDLF'
        ),
    ]

    def test_record_to_dict(self):
        """record_to_dict()"""

        for case, expected, string in self.records_and_expected:
            case = StringIO.StringIO(case)
            record = Bio.SeqIO.parse(case, 'fasta').next()
            result = fastatoflat.record_to_dict(record)
            self.assertEqual(
                    result,
                    expected
            )


    def test_fdict_to_str(self):
        """fdict_to_str()"""

        for record, case, expected in self.records_and_expected:
            result = fastatoflat.fdict_to_str(case)
            self.assertEqual(
                    result,
                    expected
            )


if __name__ == '__main__':
    unittest.main()

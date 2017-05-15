# -*- coding: utf-8 -*-
"""
Base constants for ObsPy.

:copyright:
    The ObsPy Development Team (devs@obspy.org)
:license:
    GNU Lesser General Public License, Version 3
    (https://www.gnu.org/copyleft/lesser.html)
"""
# NO IMPORTS FROM OBSPY OR FUTURE IN THIS FILE! (file gets used at
# installation time)
import sys


# XXX TODO when bumping to numpy 1.9.0: replace bytes() in io.reftek with
# np.tobytes()
HARD_DEPENDENCIES = {
    "future": ">=0.12.4",
    "numpy": ">=1.6.1",
    "scipy": ">=0.9.0",
    "matplotlib": ">=1.1.0",
    "lxml": "",
    "setuptools": "",
    "decorator": "",
    "requests": "",
    }
OPTIONAL_DEPENDENCIES = {
    'arclink': {
        "cryptography": "",
        "m2crypto": "",
        "pycrypto": ""},
    'db': {
        "sqlalchemy": ""},
    # for docs, also see conda environment file under
    # misc/docs/py3-docs-master.yml
    # other versions might work as well but these are currently used in our
    # docs buildbot and therefore confirmed to work
    'docs': {
        "sphinx": ">=1.1",
        "sphinx-bootstrap-theme": "",
        # for 'make coverage'
        "coverage": ">=3.5",
        # for 'make citations'
        "pybtex": ">=0.16",
        # for 'make docset'
        "doc2dash": "",
        # for tutorial
        # https://github.com/obspy/wheelhouse/raw/master/
        #      basemap-1.0.7-cp27-none-linux_x86_64.whl
        # https://github.com/obspy/wheelhouse/raw/master/
        #      mlpy-3.5.0-cp27-none-linux_x86_64.whl
        "basemap": "",
        "mlpy": "",
        # for doctests
        "pyproj": ""},
    'geodetics': {
        "geographiclib": ""},
    'imaging': {
        "basemap": "",
        "cartopy": ""},
    'signal': {
        "jsonschema": ">=1.0.0"},
    'nlloc-tests': {
        "pyproj": ""},
    'shapefile': {
        "gdal": ">=1.7.3"},
    'tests': {
        "flake8": ">=3.0",
        "pep8-naming": "",
        "pyimgur": ""},
    }
# add mock as optional dependency for running tests on Python 2
if sys.version_info.major == 2:
    OPTIONAL_DEPENDENCIES['tests']['mock'] = ""

DEPENDENCIES = {}
# XXX currently the case of one module being specified in different dependency
# sections is not covered, but at least what is specified in "hard
# dependencies" will always win..
for _section, _dependencies in OPTIONAL_DEPENDENCIES.items():
    DEPENDENCIES.update(_dependencies)
DEPENDENCIES.update(HARD_DEPENDENCIES)

INSTALL_REQUIRES = [''.join(spec) for spec in HARD_DEPENDENCIES.items()]
EXTRAS_REQUIRE = {
    section: list(''.join(spec) for spec in deps)
    for section, deps in OPTIONAL_DEPENDENCIES.items()}

ENTRY_POINTS = {
    'console_scripts': [
        'obspy-flinn-engdahl = obspy.scripts.flinnengdahl:main',
        'obspy-runtests = obspy.scripts.runtests:main',
        'obspy-reftek-rescue = obspy.scripts.reftekrescue:main',
        'obspy-print = obspy.scripts.print:main',
        'obspy-sds-report = obspy.scripts.sds_html_report:main',
        'obspy-indexer = obspy.db.scripts.indexer:main',
        'obspy-scan = obspy.imaging.scripts.scan:main',
        'obspy-plot = obspy.imaging.scripts.plot:main',
        'obspy-mopad = obspy.imaging.scripts.mopad:main',
        'obspy-mseed-recordanalyzer = '
        'obspy.io.mseed.scripts.recordanalyzer:main',
        'obspy-dataless2xseed = obspy.io.xseed.scripts.dataless2xseed:main',
        'obspy-xseed2dataless = obspy.io.xseed.scripts.xseed2dataless:main',
        'obspy-dataless2resp = obspy.io.xseed.scripts.dataless2resp:main',
        ],
    'obspy.plugin.waveform': [
        'TSPAIR = obspy.io.ascii.core',
        'SLIST = obspy.io.ascii.core',
        'PICKLE = obspy.core.stream',
        'CSS = obspy.io.css.core',
        'WIN = obspy.io.win.core',
        'KINEMETRICS_EVT = obspy.io.kinemetrics.core',
        'GSE1 = obspy.io.gse2.core',
        'GSE2 = obspy.io.gse2.core',
        'MSEED = obspy.io.mseed.core',
        'NNSA_KB_CORE = obspy.io.css.core',
        'PDAS = obspy.io.pdas.core',
        'SAC = obspy.io.sac.core',
        'SACXY = obspy.io.sac.core',
        'Y = obspy.io.y.core',
        'SEG2 = obspy.io.seg2.seg2',
        'SEGY = obspy.io.segy.core',
        'SU = obspy.io.segy.core',
        'SEISAN = obspy.io.seisan.core',
        'Q = obspy.io.sh.core',
        'SH_ASC = obspy.io.sh.core',
        'WAV = obspy.io.wav.core',
        'AH = obspy.io.ah.core',
        'KNET = obspy.io.nied.knet',
        'GCF = obspy.io.gcf.core',
        'REFTEK130 = obspy.io.reftek.core',
        ],
    'obspy.plugin.waveform.TSPAIR': [
        'isFormat = obspy.io.ascii.core:_is_tspair',
        'readFormat = obspy.io.ascii.core:_read_tspair',
        'writeFormat = obspy.io.ascii.core:_write_tspair',
        ],
    'obspy.plugin.waveform.SLIST': [
        'isFormat = obspy.io.ascii.core:_is_slist',
        'readFormat = obspy.io.ascii.core:_read_slist',
        'writeFormat = obspy.io.ascii.core:_write_slist',
        ],
    'obspy.plugin.waveform.PICKLE': [
        'isFormat = obspy.core.stream:_is_pickle',
        'readFormat = obspy.core.stream:_read_pickle',
        'writeFormat = obspy.core.stream:_write_pickle',
        ],
    'obspy.plugin.waveform.CSS': [
        'isFormat = obspy.io.css.core:_is_css',
        'readFormat = obspy.io.css.core:_read_css',
        ],
    'obspy.plugin.waveform.NNSA_KB_CORE': [
        'isFormat = obspy.io.css.core:_is_nnsa_kb_core',
        'readFormat = obspy.io.css.core:_read_nnsa_kb_core',
        ],
    'obspy.plugin.waveform.WIN': [
        'isFormat = obspy.io.win.core:_is_win',
        'readFormat = obspy.io.win.core:_read_win',
        ],
    'obspy.plugin.waveform.KINEMETRICS_EVT': [
        'isFormat = obspy.io.kinemetrics.core:is_evt',
        'readFormat = obspy.io.kinemetrics.core:read_evt',
        ],
    'obspy.plugin.waveform.GSE1': [
        'isFormat = obspy.io.gse2.core:_is_gse1',
        'readFormat = obspy.io.gse2.core:_read_gse1',
        ],
    'obspy.plugin.waveform.GSE2': [
        'isFormat = obspy.io.gse2.core:_is_gse2',
        'readFormat = obspy.io.gse2.core:_read_gse2',
        'writeFormat = obspy.io.gse2.core:_write_gse2',
        ],
    'obspy.plugin.waveform.MSEED': [
        'isFormat = obspy.io.mseed.core:_is_mseed',
        'readFormat = obspy.io.mseed.core:_read_mseed',
        'writeFormat = obspy.io.mseed.core:_write_mseed',
        ],
    'obspy.plugin.waveform.PDAS': [
        'isFormat = obspy.io.pdas.core:_is_pdas',
        'readFormat = obspy.io.pdas.core:_read_pdas',
        ],
    'obspy.plugin.waveform.SAC': [
        'isFormat = obspy.io.sac.core:_is_sac',
        'readFormat = obspy.io.sac.core:_read_sac',
        'writeFormat = obspy.io.sac.core:_write_sac',
        ],
    'obspy.plugin.waveform.SACXY': [
        'isFormat = obspy.io.sac.core:_is_sac_xy',
        'readFormat = obspy.io.sac.core:_read_sac_xy',
        'writeFormat = obspy.io.sac.core:_write_sac_xy',
        ],
    'obspy.plugin.waveform.SEG2': [
        'isFormat = obspy.io.seg2.seg2:_is_seg2',
        'readFormat = obspy.io.seg2.seg2:_read_seg2',
        ],
    'obspy.plugin.waveform.SEGY': [
        'isFormat = obspy.io.segy.core:_is_segy',
        'readFormat = obspy.io.segy.core:_read_segy',
        'writeFormat = obspy.io.segy.core:_write_segy',
        ],
    'obspy.plugin.waveform.SU': [
        'isFormat = obspy.io.segy.core:_is_su',
        'readFormat = obspy.io.segy.core:_read_su',
        'writeFormat = obspy.io.segy.core:_write_su',
        ],
    'obspy.plugin.waveform.SEISAN': [
        'isFormat = obspy.io.seisan.core:_is_seisan',
        'readFormat = obspy.io.seisan.core:_read_seisan',
        ],
    'obspy.plugin.waveform.Q': [
        'isFormat = obspy.io.sh.core:_is_q',
        'readFormat = obspy.io.sh.core:_read_q',
        'writeFormat = obspy.io.sh.core:_write_q',
        ],
    'obspy.plugin.waveform.SH_ASC': [
        'isFormat = obspy.io.sh.core:_is_asc',
        'readFormat = obspy.io.sh.core:_read_asc',
        'writeFormat = obspy.io.sh.core:_write_asc',
        ],
    'obspy.plugin.waveform.WAV': [
        'isFormat = obspy.io.wav.core:_is_wav',
        'readFormat = obspy.io.wav.core:_read_wav',
        'writeFormat = obspy.io.wav.core:_write_wav',
        ],
    'obspy.plugin.waveform.Y': [
        'isFormat = obspy.io.y.core:_is_y',
        'readFormat = obspy.io.y.core:_read_y',
        ],
    'obspy.plugin.waveform.AH': [
        'isFormat = obspy.io.ah.core:_is_ah',
        'readFormat = obspy.io.ah.core:_read_ah',
        'writeFormat = obspy.io.ah.core:_write_ah1',
        ],
    'obspy.plugin.waveform.KNET': [
        'isFormat = obspy.io.nied.knet:_is_knet_ascii',
        'readFormat = obspy.io.nied.knet:_read_knet_ascii',
        ],
    'obspy.plugin.waveform.GCF': [
        'isFormat = obspy.io.gcf.core:_is_gcf',
        'readFormat = obspy.io.gcf.core:_read_gcf',
        ],
    'obspy.plugin.waveform.REFTEK130': [
        'isFormat = obspy.io.reftek.core:_is_reftek130',
        'readFormat = obspy.io.reftek.core:_read_reftek130',
        ],
    'obspy.plugin.event': [
        'QUAKEML = obspy.io.quakeml.core',
        'SC3ML = obspy.io.seiscomp.event',
        'ZMAP = obspy.io.zmap.core',
        'MCHEDR = obspy.io.pde.mchedr',
        'JSON = obspy.io.json.core',
        'NDK = obspy.io.ndk.core',
        'NLLOC_HYP = obspy.io.nlloc.core',
        'NLLOC_OBS = obspy.io.nlloc.core',
        'NORDIC = obspy.io.nordic.core',
        'CNV = obspy.io.cnv.core',
        'CMTSOLUTION = obspy.io.cmtsolution.core',
        'SCARDEC = obspy.io.scardec.core',
        'SHAPEFILE = obspy.io.shapefile.core',
        'KML = obspy.io.kml.core',
        'FNETMT = obspy.io.nied.fnetmt',
        'GSE2 = obspy.io.gse2.bulletin'
        ],
    'obspy.plugin.event.QUAKEML': [
        'isFormat = obspy.io.quakeml.core:_is_quakeml',
        'readFormat = obspy.io.quakeml.core:_read_quakeml',
        'writeFormat = obspy.io.quakeml.core:_write_quakeml',
        ],
    'obspy.plugin.event.SC3ML': [
        'writeFormat = obspy.io.seiscomp.event:_write_sc3ml',
        ],
    'obspy.plugin.event.MCHEDR': [
        'isFormat = obspy.io.pde.mchedr:_is_mchedr',
        'readFormat = obspy.io.pde.mchedr:_read_mchedr',
        ],
    'obspy.plugin.event.JSON': [
        'writeFormat = obspy.io.json.core:_write_json',
        ],
    'obspy.plugin.event.ZMAP': [
        'isFormat = obspy.io.zmap.core:_is_zmap',
        'readFormat = obspy.io.zmap.core:_read_zmap',
        'writeFormat = obspy.io.zmap.core:_write_zmap',
        ],
    'obspy.plugin.event.CNV': [
        'writeFormat = obspy.io.cnv.core:_write_cnv',
        ],
    'obspy.plugin.event.NDK': [
        'isFormat = obspy.io.ndk.core:_is_ndk',
        'readFormat = obspy.io.ndk.core:_read_ndk',
        ],
    'obspy.plugin.event.NLLOC_HYP': [
        'isFormat = obspy.io.nlloc.core:is_nlloc_hyp',
        'readFormat = obspy.io.nlloc.core:read_nlloc_hyp',
        ],
    'obspy.plugin.event.NLLOC_OBS': [
        'writeFormat = obspy.io.nlloc.core:write_nlloc_obs',
        ],
    'obspy.plugin.event.NORDIC': [
        'writeFormat = obspy.io.nordic.core:write_select',
        'readFormat = obspy.io.nordic.core:read_nordic',
        'isFormat = obspy.io.nordic.core:_is_sfile'
        ],
    'obspy.plugin.event.CMTSOLUTION': [
        'isFormat = obspy.io.cmtsolution.core:_is_cmtsolution',
        'readFormat = obspy.io.cmtsolution.core:_read_cmtsolution',
        'writeFormat = obspy.io.cmtsolution.core:_write_cmtsolution'
        ],
    'obspy.plugin.event.SCARDEC': [
        'isFormat = obspy.io.scardec.core:_is_scardec',
        'readFormat = obspy.io.scardec.core:_read_scardec',
        'writeFormat = obspy.io.scardec.core:_write_scardec'
        ],
    'obspy.plugin.event.FNETMT': [
        'isFormat = obspy.io.nied.fnetmt:_is_fnetmt_catalog',
        'readFormat = obspy.io.nied.fnetmt:_read_fnetmt_catalog',
        ],
    'obspy.plugin.event.GSE2': [
        'isFormat = obspy.io.gse2.bulletin:_is_gse2',
        'readFormat = obspy.io.gse2.bulletin:_read_gse2',
        ],
    'obspy.plugin.event.SHAPEFILE': [
        'writeFormat = obspy.io.shapefile.core:_write_shapefile',
        ],
    'obspy.plugin.event.KML': [
        'writeFormat = obspy.io.kml.core:_write_kml',
        ],
    'obspy.plugin.inventory': [
        'STATIONXML = obspy.io.stationxml.core',
        'INVENTORYXML = obspy.io.arclink.inventory',
        'SC3ML = obspy.io.seiscomp.sc3ml',
        'SACPZ = obspy.io.sac.sacpz',
        'CSS = obspy.io.css.station',
        'SHAPEFILE = obspy.io.shapefile.core',
        'STATIONTXT = obspy.io.stationtxt.core',
        'KML = obspy.io.kml.core'
        ],
    'obspy.plugin.inventory.STATIONXML': [
        'isFormat = obspy.io.stationxml.core:_is_stationxml',
        'readFormat = obspy.io.stationxml.core:_read_stationxml',
        'writeFormat = obspy.io.stationxml.core:_write_stationxml',
        ],
    'obspy.plugin.inventory.INVENTORYXML': [
        'isFormat = obspy.io.arclink.inventory:_is_inventory_xml',
        'readFormat = obspy.io.arclink.inventory:_read_inventory_xml',
        ],
    'obspy.plugin.inventory.SC3ML': [
        'isFormat = obspy.io.seiscomp.sc3ml:_is_sc3ml',
        'readFormat = obspy.io.seiscomp.sc3ml:_read_sc3ml',
        ],
    'obspy.plugin.inventory.SACPZ': [
        'writeFormat = obspy.io.sac.sacpz:_write_sacpz',
        ],
    'obspy.plugin.inventory.CSS': [
        'writeFormat = obspy.io.css.station:_write_css',
        ],
    'obspy.plugin.inventory.SHAPEFILE': [
        'writeFormat = obspy.io.shapefile.core:_write_shapefile',
        ],
    'obspy.plugin.inventory.STATIONTXT': [
        'isFormat = obspy.io.stationtxt.core:is_fdsn_station_text_file',
        'readFormat = '
        'obspy.io.stationtxt.core:read_fdsn_station_text_file',
        'writeFormat = obspy.io.stationtxt.core:_write_stationtxt',
        ],
    'obspy.plugin.inventory.KML': [
        'writeFormat = obspy.io.kml.core:_write_kml',
        ],
    'obspy.plugin.detrend': [
        'linear = scipy.signal:detrend',
        'constant = scipy.signal:detrend',
        'demean = scipy.signal:detrend',
        'simple = obspy.signal.detrend:simple',
        'polynomial = obspy.signal.detrend:polynomial',
        'spline = obspy.signal.detrend:spline'
        ],
    'obspy.plugin.differentiate': [
        'gradient = numpy:gradient',
        ],
    'obspy.plugin.integrate': [
        'cumtrapz = '
        'obspy.signal.differentiate_and_integrate:integrate_cumtrapz',
        'spline = '
        'obspy.signal.differentiate_and_integrate:integrate_spline',
        ],
    'obspy.plugin.filter': [
        'bandpass = obspy.signal.filter:bandpass',
        'bandstop = obspy.signal.filter:bandstop',
        'lowpass = obspy.signal.filter:lowpass',
        'highpass = obspy.signal.filter:highpass',
        'lowpass_cheby_2 = obspy.signal.filter:lowpass_cheby_2',
        'lowpass_fir = obspy.signal.filter:lowpass_FIR',
        'remez_fir = obspy.signal.filter:remez_FIR',
        ],
    'obspy.plugin.interpolate': [
        'interpolate_1d = obspy.signal.interpolation:interpolate_1d',
        'weighted_average_slopes = '
        'obspy.signal.interpolation:weighted_average_slopes',
        'lanczos = obspy.signal.interpolation:lanczos_interpolation'
        ],
    'obspy.plugin.rotate': [
        'rotate_ne_rt = obspy.signal.rotate:rotate_ne_rt',
        'rotate_rt_ne = obspy.signal.rotate:rotate_rt_ne',
        'rotate_zne_lqt = obspy.signal.rotate:rotate_zne_lqt',
        'rotate_lqt_zne = obspy.signal.rotate:rotate_lqt_zne'
        ],
    'obspy.plugin.taper': [
        'cosine = obspy.signal.invsim:cosine_taper',
        'barthann = scipy.signal:barthann',
        'bartlett = scipy.signal:bartlett',
        'blackman = scipy.signal:blackman',
        'blackmanharris = scipy.signal:blackmanharris',
        'bohman = scipy.signal:bohman',
        'boxcar = scipy.signal:boxcar',
        'chebwin = scipy.signal:chebwin',
        'flattop = scipy.signal:flattop',
        'gaussian = scipy.signal:gaussian',
        'general_gaussian = scipy.signal:general_gaussian',
        'hamming = scipy.signal:hamming',
        'hann = scipy.signal:hann',
        'kaiser = scipy.signal:kaiser',
        'nuttall = scipy.signal:nuttall',
        'parzen = scipy.signal:parzen',
        'slepian = scipy.signal:slepian',
        'triang = scipy.signal:triang',
        ],
    'obspy.plugin.trigger': [
        'recstalta = obspy.signal.trigger:recursive_sta_lta',
        'carlstatrig = obspy.signal.trigger:carl_sta_trig',
        'classicstalta = obspy.signal.trigger:classic_sta_lta',
        'delayedstalta = obspy.signal.trigger:delayed_sta_lta',
        'zdetect = obspy.signal.trigger:z_detect',
        'recstaltapy = obspy.signal.trigger:recursive_sta_lta_py',
        'classicstaltapy = obspy.signal.trigger:classic_sta_lta_py',
        ],
    'obspy.db.feature': [
        'minmax_amplitude = obspy.db.feature:MinMaxAmplitudeFeature',
        'bandpass_preview = obspy.db.feature:BandpassPreviewFeature',
        ],
    }

# defining ObsPy modules currently used by runtests and the path function
DEFAULT_MODULES = ['clients.filesystem', 'core', 'db', 'geodetics', 'imaging',
                   'io.ah', 'io.arclink', 'io.ascii', 'io.cmtsolution',
                   'io.cnv', 'io.css', 'io.win', 'io.gcf', 'io.gse2',
                   'io.json', 'io.kinemetrics', 'io.kml', 'io.mseed', 'io.ndk',
                   'io.nied', 'io.nlloc', 'io.nordic', 'io.pdas', 'io.pde',
                   'io.quakeml', 'io.reftek', 'io.sac', 'io.scardec',
                   'io.seg2', 'io.segy', 'io.seisan', 'io.sh', 'io.shapefile',
                   'io.seiscomp', 'io.stationtxt', 'io.stationxml', 'io.wav',
                   'io.xseed', 'io.y', 'io.zmap', 'realtime', 'scripts',
                   'signal', 'taup']
NETWORK_MODULES = ['clients.arclink', 'clients.earthworm', 'clients.fdsn',
                   'clients.iris', 'clients.neic', 'clients.seedlink',
                   'clients.seishub', 'clients.syngine']
ALL_MODULES = DEFAULT_MODULES + NETWORK_MODULES

# default order of automatic format detection
WAVEFORM_PREFERRED_ORDER = ['MSEED', 'SAC', 'GSE2', 'SEISAN', 'SACXY', 'GSE1',
                            'Q', 'SH_ASC', 'SLIST', 'TSPAIR', 'Y', 'PICKLE',
                            'SEGY', 'SU', 'SEG2', 'WAV', 'WIN', 'CSS',
                            'NNSA_KB_CORE', 'AH', 'PDAS', 'KINEMETRICS_EVT',
                            'GCF']
EVENT_PREFERRED_ORDER = ['QUAKEML', 'NLLOC_HYP']
# waveform plugins accepting a byteorder keyword
WAVEFORM_ACCEPT_BYTEORDER = ['MSEED', 'Q', 'SAC', 'SEGY', 'SU']

NATIVE_BYTEORDER = sys.byteorder == 'little' and '<' or '>'

KEYWORDS = [
    'ArcLink', 'array', 'array analysis', 'ASC', 'beachball',
    'beamforming', 'cross correlation', 'database', 'dataless',
    'Dataless SEED', 'win', 'earthquakes', 'Earthworm', 'EIDA',
    'envelope', 'ESRI', 'events', 'FDSN', 'features', 'filter',
    'focal mechanism', 'GCF', 'GSE1', 'GSE2', 'hob', 'Tau-P', 'imaging',
    'instrument correction', 'instrument simulation', 'IRIS', 'kinemetrics',
    'KML', 'magnitude', 'MiniSEED', 'misfit', 'mopad', 'MSEED', 'NDK', 'NERA',
    'NERIES', 'NonLinLoc', 'NLLOC', 'Nordic', 'observatory', 'ORFEUS', 'PDAS',
    'picker', 'processing', 'PQLX', 'Q', 'real time', 'realtime', 'REFTEK',
    'REFTEK130', 'RT-130', 'RESP', 'response file', 'RT', 'SAC', 'scardec',
    'sc3ml', 'SDS', 'SEED', 'SeedLink', 'SEG-2', 'SEG Y', 'SEISAN', 'SeisHub',
    'Seismic Handler', 'seismology', 'seismogram', 'seismograms',
    'shapefile', 'signal', 'slink', 'spectrogram', 'StationXML', 'taper',
    'taup', 'travel time', 'trigger', 'VERCE', 'WAV', 'waveform',
    'WaveServer', 'WaveServerV', 'WebDC', 'web service', 'Winston',
    'XML-SEED', 'XSEED']
import os
from typing import Optional

from qgis.core import (QgsApplication, QgsCoordinateReferenceSystem, QgsProject, QgsRasterLayer, QgsRectangle,
                       QgsVectorLayer)
from qgis.PyQt.QtWidgets import QWidget

from deepness.common.channels_mapping import ChannelsMapping, ImageChannelCompositeByte, ImageChannelStandaloneBand

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, 'data'))


def get_dummy_segmentation_model_path():
    """
    Get path of a dummy onnx model. See details in README in model directory.
    Model used for unit tests processing purposes
    """
    return os.path.join(TEST_DATA_DIR, 'dummy_model', 'dummy_segmentation_models', 'dummy_model.onnx')


def get_dummy_sigmoid_model_path():
    """
    Get path of a dummy onnx model. See details in README in model directory.
    Model used for unit tests processing purposes
    """
    return os.path.join(TEST_DATA_DIR, 'dummy_model', 'one_output_sigmoid_red_detector.onnx')


def get_dummy_segmentation_model_different_output_size_path():
    """
    Get path of a dummy onnx model. See details in README in model directory.
    Model used for unit tests processing purposes. Its output size is different than input size.
    """
    return os.path.join(TEST_DATA_DIR, 'dummy_model', 'dummy_segmentation_models', 'different_output_size_512_to_484.onnx')


def get_dummy_segmentation_models_dict():
    """
    Get dictionary with dummy segmentation models paths. See details in README in model directory.
    Models used for unit tests processing purposes
    """
    return {
        'one_output': {
            '1x1x512x512': os.path.join(TEST_DATA_DIR, 'dummy_model', 'dummy_segmentation_models', 'one_output_sigmoid_bsx1x512x512.onnx'),
            '1x512x512': os.path.join(TEST_DATA_DIR, 'dummy_model', 'dummy_segmentation_models', 'one_output_sigmoid_bsx512x512.onnx'),
            '1x2x512x512': os.path.join(TEST_DATA_DIR, 'dummy_model', 'dummy_segmentation_models', 'one_output_softmax_bsx2x512x512.onnx'),
        },
        'two_outputs': {
            '1x1x512x512': os.path.join(TEST_DATA_DIR, 'dummy_model', 'dummy_segmentation_models', 'two_outputs_sigmoid_bsx1x512x512.onnx'),
            '1x512x512': os.path.join(TEST_DATA_DIR, 'dummy_model', 'dummy_segmentation_models', 'two_outputs_sigmoid_bsx512x512.onnx'),
            '1x2x512x512': os.path.join(TEST_DATA_DIR, 'dummy_model', 'dummy_segmentation_models', 'two_outputs_softmax_bsx2x512x512.onnx'),
        }
    }


def get_dummy_recognition_model_path():
    """
    Get path of a dummy onnx model. See details in README in model directory.
    Model used for unit tests processing purposes
    """
    return os.path.join(TEST_DATA_DIR, 'dummy_model', 'dummy_recognition_model.onnx')


def get_dummy_recognition_image_path():
    """
    Get path of a dummy image, which can be used for testing with conjunction with dummy_mode (see get_dummy_model_path)
    """
    return os.path.join(TEST_DATA_DIR, 'dummy_recognition_image.png')


def get_dummy_recognition_map_path():
    """
    Get path of a dummy map, which can be used for testing with conjunction with dummy_mode (see get_dummy_model_path)
    """
    return os.path.join(TEST_DATA_DIR, 'dummy_recognition_map.tif')


def get_dummy_regression_model_path():
    """
    Get path of a dummy onnx model. See details in README in model directory.
    Model used for unit tests processing purposes
    """
    return os.path.join(TEST_DATA_DIR, 'dummy_model', 'dummy_regression_models', 'dummy_regression_model.onnx')


def get_dummy_regression_model_path_batched():
    """
    Get path of a dummy onnx model. See details in README in model directory.
    Model used for unit tests processing purposes
    """
    return os.path.join(TEST_DATA_DIR, 'dummy_model', 'dummy_regression_models', 'dummy_regression_model_batched.onnx')


def get_dummy_regression_models_dict():
    """
    Get dictionary with dummy regression models paths. See details in README in model directory.
    Models used for unit tests processing purposes
    """
    return {
        'one_output': {
            '1x1x512x512': os.path.join(TEST_DATA_DIR, 'dummy_model', 'dummy_regression_models', 'one_output_sigmoid_bsx1x512x512.onnx'),
            '1x512x512': os.path.join(TEST_DATA_DIR, 'dummy_model', 'dummy_regression_models', 'one_output_sigmoid_bsx512x512.onnx'),
        },
        'two_outputs': {
            '1x1x512x512': os.path.join(TEST_DATA_DIR, 'dummy_model', 'dummy_regression_models', 'two_outputs_sigmoid_bsx1x512x512.onnx'),
            '1x512x512': os.path.join(TEST_DATA_DIR, 'dummy_model', 'dummy_regression_models', 'two_outputs_sigmoid_bsx512x512.onnx'),
        }
    }


def get_dummy_superresolution_model_path():
    """
    Get path of a dummy onnx model. See details in README in model directory.
    Model used for unit tests processing purposes
    """
    return os.path.join(TEST_DATA_DIR, 'dummy_model', 'dummy_superresolution_model.onnx')


def get_dummy_fotomap_small_path():
    """
    Get path of dummy fotomap tif file, which can be used
    for testing with conjunction with dummy_mode (see get_dummy_model_path)
    """
    return os.path.join(TEST_DATA_DIR, 'dummy_fotomap_small.tif')


def get_dummy_fotomap_area_path():
    """
    Get path of the file with processing area polygon, for dummy_fotomap (see get_dummy_fotomap_small_path)
    """
    return os.path.join(TEST_DATA_DIR, 'dummy_fotomap_area.gpkg')


def get_dummy_fotomap_area_crs3857_path():
    """
    Get path of the file with processing area polygon (but in crs 3857), for dummy_fotomap (see get_dummy_fotomap_small_path)
    """
    return os.path.join(TEST_DATA_DIR, 'dummy_fotomap_area_3857.gpkg')


def get_predicted_detections_path():
    """
    Get path of the file with predicted detections, for testing purposes
    """
    return os.path.join(TEST_DATA_DIR, 'test_bounding_boxes.npy')


def create_rlayer_from_file(file_path):
    """
    Create raster layer from tif file and add it to current QgsProject
    """
    rlayer = QgsRasterLayer(file_path, 'fotomap')
    if rlayer.width() == 0:
        raise Exception("0 width - rlayer not loaded properly. Probably invalid file path?")
    rlayer.setCrs(QgsCoordinateReferenceSystem("EPSG:32633"))
    QgsProject.instance().addMapLayer(rlayer)
    return rlayer


def create_vlayer_from_file(file_path):
    """
    Create vector layer from geometry file and add it to current QgsProject
    """
    vlayer = QgsVectorLayer(file_path)
    if not vlayer.isValid():
        raise Exception("Invalid vlayer! Probably invalid file path?")
    QgsProject.instance().addMapLayer(vlayer)
    return vlayer


def create_default_input_channels_mapping_for_rgba_bands():
    # as in 'set_rlayer' function in 'input_channels_mapping_widget'

    channels_mapping = ChannelsMapping()
    channels_mapping.set_image_channels(
        [
            ImageChannelStandaloneBand(band_number=1, name='red'),
            ImageChannelStandaloneBand(band_number=2, name='green'),
            ImageChannelStandaloneBand(band_number=3, name='blue'),
            ImageChannelStandaloneBand(band_number=4, name='alpha'),
        ]
    )
    channels_mapping.set_number_of_model_inputs_same_as_image_channels()
    return channels_mapping


def create_default_input_channels_mapping_for_rgb_bands():
    # as in 'set_rlayer' function in 'input_channels_mapping_widget'

    channels_mapping = ChannelsMapping()
    channels_mapping.set_image_channels(
        [
            ImageChannelStandaloneBand(band_number=1, name='red'),
            ImageChannelStandaloneBand(band_number=2, name='green'),
            ImageChannelStandaloneBand(band_number=3, name='blue'),
        ]
    )
    channels_mapping.set_number_of_model_inputs_same_as_image_channels()
    return channels_mapping


def create_default_input_channels_mapping_for_google_satellite_bands():
    # as in 'set_rlayer' function in 'input_channels_mapping_widget'

    channels_mapping = ChannelsMapping()
    channels_mapping.set_number_of_model_inputs(3)
    channels_mapping.set_image_channels(
        [
            ImageChannelCompositeByte(byte_number=2, name='red'),
            ImageChannelCompositeByte(byte_number=1, name='green'),
            ImageChannelCompositeByte(byte_number=0, name='blue'),
            ImageChannelCompositeByte(byte_number=3, name='alpha'),
        ]
    )
    return channels_mapping


class SignalCollector(QWidget):
    """
    Allows to intercept a signal and collect its data during unit testing
    """

    def __init__(self, signal_to_collect):
        super().__init__()
        self.was_called = False
        self.signal_args = None
        self.signal_kwargs = None
        signal_to_collect.connect(self.any_slot)

    def any_slot(self, *args, **kwargs):
        self.signal_kwargs = kwargs
        self.signal_args = args
        self.was_called = True

    def get_first_arg(self):
        assert self.was_called
        if self.signal_args:
            return self.signal_args[0]
        if self.signal_kwargs:
            return list(self.signal_kwargs.values())[0]
        raise Exception("No argument were provided for the signal!")


_APP_INSTANCE: Optional[QgsApplication] = None


def init_qgis():
    print("Initializing QGIS")
    global _APP_INSTANCE
    if _APP_INSTANCE:
        print("QGIS already initialized")
        return _APP_INSTANCE

    print("QGIS not initialized yet")
    qgs = QgsApplication([b''], GUIenabled=False)
    qgs.setPrefixPath('/usr/bin/qgis', True)
    qgs.initQgis()
    _APP_INSTANCE = qgs
    return _APP_INSTANCE

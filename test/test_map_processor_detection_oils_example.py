from unittest.mock import MagicMock
import cv2
import numpy as np
import matplotlib.pyplot as plt

from deepness.common.processing_parameters.detection_parameters import DetectionParameters
from deepness.common.processing_parameters.map_processing_parameters import ProcessedAreaType, \
    ModelOutputFormat
from deepness.processing.map_processor.map_processor_detection import MapProcessorDetection
from deepness.processing.models.detector import Detector
from test.test_utils import init_qgis, create_rlayer_from_file, \
    create_default_input_channels_mapping_for_rgb_bands

import os

from pathlib import Path

HOME_DIR = Path(__file__).resolve().parents[1]
EXAMPLE_DATA_DIR = os.path.join(HOME_DIR, 'examples', 'yolov5_oils_detection_bing_map')

MODEL_FILE_PATH = os.path.join(EXAMPLE_DATA_DIR, 'model_yolov5_m_oils_512_1c.onnx')
RASTER_FILE_PATH = os.path.join(EXAMPLE_DATA_DIR, 'oils.tif')

INPUT_CHANNELS_MAPPING = create_default_input_channels_mapping_for_rgb_bands()


def test_map_processor_detection_oil_example():
    qgs = init_qgis()
    rlayer = create_rlayer_from_file(RASTER_FILE_PATH)

    model_wrapper = Detector(MODEL_FILE_PATH)

    params = DetectionParameters(
        resolution_cm_per_px=150,
        tile_size_px=model_wrapper.get_input_size_in_pixels()[0],  # same x and y dimensions, so take x
        processed_area_type=ProcessedAreaType.ENTIRE_LAYER,
        mask_layer_id=None,
        input_layer_id=rlayer.id(),
        input_channels_mapping=INPUT_CHANNELS_MAPPING,
        processing_overlap_percentage=40,
        model=model_wrapper,
        confidence=0.5,
        iou_threshold=0.1,
        model_output_format=ModelOutputFormat.ALL_CLASSES_AS_SEPARATE_LAYERS,
        model_output_format__single_class_number=-1,
    )

    map_processor = MapProcessorDetection(
        rlayer=rlayer,
        vlayer_mask=None,
        map_canvas=MagicMock(),
        params=params,
    )

    map_processor.run()

    # dets = map_processor.get_all_detections()
    # im = np.zeros((map_processor.base_extent_bbox_in_full_image.y_max, map_processor.base_extent_bbox_in_full_image.x_max), dtype=np.uint8)
    #
    # for bb in dets:
    #     cv2.rectangle(im, (bb.bbox.x_min, bb.bbox.y_min), (bb.bbox.x_max, bb.bbox.y_max), 255, 2)
    #
    # plt.imshow(im)
    # plt.show()


if __name__ == '__main__':
    test_map_processor_detection_oil_example()
    print('Done')

## libreries
import numpy as np
import supervision as sv
from tqdm import tqdm
import time
from ultralytics import YOLO

COLORS = sv.ColorPalette.from_hex(["#E6194B", "#3CB44B", "#FFE119", "#3C76D1"])

def video_test(model_path, video_path, store_video_path):
    model = YOLO(model_path)
    SOURCE_VIDEO_PATH = video_path
    TARGET_VIDEO_PATH = store_video_path

    LINE_1_START = sv.Point(490, 320)
    LINE_1_END = sv.Point(1200, 250)

    LINE_2_START = sv.Point(1370, 280)
    LINE_2_END = sv.Point(1850, 460)

    LINE_3_START = sv.Point(450, 1020)
    LINE_3_END = sv.Point(1880, 570)

    LINE_4_START = sv.Point(400, 350)
    LINE_4_END = sv.Point(420, 1000)


    LINE_ZONE_1 = sv.LineZone(
        start=LINE_1_START,
        end=LINE_1_END,
        triggering_anchors=(sv.Position.BOTTOM_CENTER,)
    )

    LINE_ZONE_2 = sv.LineZone(
        start=LINE_2_START,
        end=LINE_2_END,
        triggering_anchors=(sv.Position.BOTTOM_CENTER,)
    )

    LINE_ZONE_3 = sv.LineZone(
        start=LINE_3_START,
        end=LINE_3_END,
        triggering_anchors=(sv.Position.BOTTOM_CENTER,)
    )

    LINE_ZONE_4 = sv.LineZone(
        start=LINE_4_START,
        end=LINE_4_END,
        triggering_anchors=(sv.Position.BOTTOM_CENTER,)
    )

    #POLYGON_ZONE = sv.PolygonZone(
    #    polygon=POLYGON,
    #    triggering_anchors=(sv.Position.CENTER,)
    #)

    LINE_ZONE_ANNOTATOR = sv.LineZoneAnnotator(
        text_scale=0.8,
        text_orient_to_line=True,
        display_text_box=True,
        text_centered=False
    )

    LINE_ZONE_ANNOTATOR_MULTICLASS = sv.LineZoneAnnotatorMulticlass(
        text_scale=0.8,
        text_thickness=2,
        table_margin=20
    )

    COLOR_ANNOTATOR = sv.ColorAnnotator(color=COLORS)
    LABEL_ANNOTATOR = sv.LabelAnnotator(
        color=COLORS,
        text_scale=0.7,
        text_thickness=2,
        text_position=sv.Position.BOTTOM_CENTER
    )
    TRACK_ANNOTATOR = sv.TraceAnnotator(
        color=COLORS,
        trace_length=60 * 2
    )

    TRACKER = sv.ByteTrack(minimum_consecutive_frames=5)
    TRACKER.reset()

    frame_generator = sv.get_video_frames_generator(SOURCE_VIDEO_PATH)#, start=60 * 10, end=60 * 70)
    video_info = sv.VideoInfo.from_video_path(SOURCE_VIDEO_PATH)
    video_sink = sv.VideoSink(TARGET_VIDEO_PATH, video_info=video_info)

    with video_sink:
        for frame_idx, frame in tqdm(enumerate(frame_generator)):

            result = model(frame, conf=0.35, imgsz=1280, verbose=False)[0]
            detections = sv.Detections.from_ultralytics(result)
            detections = detections.with_nms(class_agnostic=True)
            #detections = detections[POLYGON_ZONE.trigger(detections)]
            detections = TRACKER.update_with_detections(detections)

            if detections['class_name'] is None or len(detections['class_name']) == 0:
                detections['class_name'] = []

            labels = [
                f"{class_name} {confidence:.2f}"
                for class_name, confidence
                in zip(detections["class_name"], detections.confidence)
            ]

            LINE_ZONE_1.trigger(detections)
            LINE_ZONE_2.trigger(detections)
            LINE_ZONE_3.trigger(detections)
            LINE_ZONE_4.trigger(detections)

            annotated_frame = frame.copy()
            #annotated_frame = sv.draw_polygon(
            #    scene=annotated_frame,
            #    polygon=POLYGON,
            #    color=sv.Color.WHITE,
            #    thickness=3
            #)

            annotated_frame = COLOR_ANNOTATOR.annotate(
                annotated_frame, detections)
            annotated_frame = LABEL_ANNOTATOR.annotate(
                annotated_frame, detections,
                labels=labels)
            annotated_frame = TRACK_ANNOTATOR.annotate(
                annotated_frame, detections)

            annotated_frame = LINE_ZONE_ANNOTATOR.annotate(
                frame=annotated_frame, line_counter=LINE_ZONE_1
            )
            annotated_frame = LINE_ZONE_ANNOTATOR.annotate(
                frame=annotated_frame, line_counter=LINE_ZONE_2
            )
            annotated_frame = LINE_ZONE_ANNOTATOR.annotate(
                frame=annotated_frame, line_counter=LINE_ZONE_3
            )
            annotated_frame = LINE_ZONE_ANNOTATOR.annotate(
                frame=annotated_frame, line_counter=LINE_ZONE_4
            )
            annotated_frame = LINE_ZONE_ANNOTATOR_MULTICLASS.annotate(
                frame=annotated_frame,
                line_zones=[LINE_ZONE_1, LINE_ZONE_2, LINE_ZONE_3, LINE_ZONE_4]
            )

            # Display the frame live
            #cv2.imshow("Live Frame", annotated_frame)
            #if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit early
            #   break

            video_sink.write_frame(annotated_frame)
    return print('finished')
def calculate_iou(boxA, boxB):
    # Calculate the intersection over union (IoU) of two bounding boxes.
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])

    interArea = max(0, xB - xA) * max(0, yB - yA)

    boxAArea = (boxA[2] - boxA[0]) * (boxA[3] - boxA[1])
    boxBArea = (boxB[2] - boxB[0]) * (boxB[3] - boxB[1])

    iou = interArea / float(boxAArea + boxBArea - interArea) if (boxAArea + boxBArea - interArea) > 0 else 0

    return iou


def bbox_area(box):
    # Calculate the area of a bounding box.
    return (box[2] - box[0]) * (box[3] - box[1]) if (box[2] > box[0] and box[3] > box[1]) else 0


def non_max_suppression(boxes, scores, threshold):
    # Perform non-maximum suppression to eliminate redundant overlapping boxes.
    if len(boxes) == 0:
        return []

    # Convert boxes to float
    boxes = boxes.astype(float)

    # Initialize the list of picked indexes
    pick = []

    # Grab the coordinates of the bounding boxes
    x1 = boxes[:, 0]
    y1 = boxes[:, 1]
    x2 = boxes[:, 2]
    y2 = boxes[:, 3]

    # Compute the area of the bounding boxes and sort the bounding boxes by the score
    area = (x2 - x1 + 1) * (y2 - y1 + 1)
    idxs = scores.argsort()[::-1]

    while len(idxs) > 0:
        # Grab the last index
        last = len(idxs) - 1
        i = idxs[last]
        pick.append(i)

        # Find the intersection area
        xx1 = np.maximum(x1[i], x1[idxs[:last]])
        yy1 = np.maximum(y1[i], y1[idxs[:last]])
        xx2 = np.minimum(x2[i], x2[idxs[:last]])
        yy2 = np.minimum(y2[i], y2[idxs[:last]])

        w = np.maximum(0, xx2 - xx1 + 1)
        h = np.maximum(0, yy2 - yy1 + 1)
        inter = w * h

        # Compute the ratio of overlap
        overlap = inter / (area[i] + area[idxs[:last]] - inter)

        # Delete all indexes from the index list that have overlap greater than the threshold
        idxs = np.delete(idxs, np.concatenate(([last], np.where(overlap > threshold)[0])))

    return boxes[pick].astype("int")
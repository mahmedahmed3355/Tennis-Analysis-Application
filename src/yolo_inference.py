def load_model(model_path):
    # Load the YOLO model from the specified path
    model = cv2.dnn.readNetFromDarknet(model_path + '.cfg', model_path + '.weights')
    return model

def perform_inference(model, image):
    # Prepare the image for the model
    blob = cv2.dnn.blobFromImage(image, 1/255.0, (416, 416), swapRB=True, crop=False)
    model.setInput(blob)
    
    # Get the output layer names
    layer_names = model.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in model.getUnconnectedOutLayers()]
    
    # Perform inference
    outputs = model.forward(output_layers)
    return outputs

def process_outputs(outputs, confidence_threshold=0.5):
    boxes = []
    confidences = []
    class_ids = []
    
    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > confidence_threshold:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                
                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
    
    return boxes, confidences, class_ids

def draw_predictions(image, boxes, confidences, class_ids, classes):
    # Draw bounding boxes and labels on the image
    for i in range(len(boxes)):
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]])
        confidence = confidences[i]
        color = (0, 255, 0)  # Green color for bounding box
        cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
        cv2.putText(image, f"{label}: {confidence:.2f}", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    
    return image

def run_yolo_inference(image_path, model_path, classes_file):
    # Load classes
    with open(classes_file, 'r') as f:
        classes = [line.strip() for line in f.readlines()]
    
    # Load model
    model = load_model(model_path)
    
    # Read image
    image = cv2.imread(image_path)
    height, width = image.shape[:2]
    
    # Perform inference
    outputs = perform_inference(model, image)
    
    # Process outputs
    boxes, confidences, class_ids = process_outputs(outputs)
    
    # Draw predictions
    result_image = draw_predictions(image, boxes, confidences, class_ids, classes)
    
    return result_image
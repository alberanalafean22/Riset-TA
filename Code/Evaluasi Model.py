y_pred = model.predict(x_test)
y_pred_bin = (y_pred > 0.5).astype(np.uint8)
y_true_bin = y_test.astype(np.uint8)

def calculate_metrics_np(y_true, y_pred):
    smooth = 1e-7
    y_true_f = y_true.flatten()
    y_pred_f = y_pred.flatten()

    intersection = np.sum(y_true_f * y_pred_f)
    union = np.sum(y_true_f) + np.sum(y_pred_f)

    dice = (2. * intersection + smooth) / (union + smooth)
    iou = (intersection + smooth) / (np.sum(y_true_f) + np.sum(y_pred_f) - intersection + smooth)
    return dice, iou

dice_score, iou_score = calculate_metrics_np(y_true_bin, y_pred_bin)
acc_score = accuracy_score(y_true_bin.flatten(), y_pred_bin.flatten())
bce = BinaryCrossentropy()(y_test, y_pred).numpy()
function drawFaceData(canvasId, imgId, faceData) {
  const canvas = document.getElementById(canvasId);
  const ctx = canvas.getContext('2d');
  const image = new Image();
  const canvasSize = 500;

  image.onload = function () {

    let scale = Math.min(canvasSize / image.width, canvasSize / image.height);
    let scaleX = (canvasSize - image.width * scale) / 2;
    let scaleY = (canvasSize - image.height * scale) / 2;

    canvas.width = canvasSize;
    canvas.height = canvasSize;

    ctx.drawImage(image, scaleX, scaleY, image.width * scale, image.height * scale);

    const box = faceData.BoundingBox;
    ctx.beginPath();
    ctx.rect(scaleX + box[0] * scale, scaleY + box[1] * scale, box[2] * scale, box[3] * scale);
    ctx.strokeStyle = 'red';
    ctx.stroke();

    Object.values(faceData.Landmarks).flat().forEach(function (landmark) {
      ctx.beginPath();
      ctx.arc(scaleX + landmark[0] * scale, scaleY + landmark[1] * scale, 2, 0, 2 * Math.PI);
      ctx.fillStyle = 'green';
      ctx.fill();
    });
  };

  image.src = document.getElementById(imgId).src;
}

function drawFaceData(canvasId, imgId, faceData) {
  const canvas = document.getElementById(canvasId);
  const ctx = canvas.getContext('2d');
  const image = new Image();
  const canvasSize = 500; 

  image.onload = function() {

    let scale = Math.min(canvasSize / image.width, canvasSize / image.height);
    let scaleX = (canvasSize - image.width * scale) / 2;
    let scaleY = (canvasSize - image.height * scale) / 2;

    // Ajusta o tamanho do canvas para 100x100
    canvas.width = canvasSize;
    canvas.height = canvasSize;

          // Desenha a imagem no canvas
    ctx.drawImage(image, x, y, image.width * scale, image.height * scale);

    // Ajusta e desenha a caixa delimitadora
    const box = identData.BoundingBox;
    ctx.beginPath();
    ctx.rect(x + box[0] * scale, y + box[1] * scale, box[2] * scale, box[3] * scale);
    ctx.strokeStyle = 'red';
    ctx.stroke();

    // Desenha os pontos de referência
    Object.values(identData.Landmarks).flat().forEach(function(landmark) {
        ctx.beginPath();
        ctx.arc(x + landmark[0] * scale, y + landmark[1] * scale, 5, 0, 2 * Math.PI);
        ctx.fillStyle = 'green';
        ctx.fill();
    });
  };

  // Define o src da imagem após configurar o onload para garantir que o evento seja capturado
  image.src = document.getElementById(imgId).src;
}

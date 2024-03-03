const referenceImage = document.getElementById('reference-image');
const comparedImage = document.getElementById('compared-image');
const resultElement = document.getElementById('result');

const compareFaces = async () => {
    const formData = new FormData();
    formData.append('reference_image', referenceImage.files[0]);
    formData.append('compared_image', comparedImage.files[0]);

    const response = await fetch('/compare', {
        method: 'POST',
        body: formData
    });

    const result = await response.json();
    resultElement.textContent = `Resultado: ${result.name}`;
};

referenceImage.addEventListener('change', compareFaces);
comparedImage.addEventListener('change', compareFaces);

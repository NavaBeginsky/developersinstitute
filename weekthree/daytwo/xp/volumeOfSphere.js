
function calculateVolume(radius){
    return 4/3 * Math.PI * Math.pow(radius, 3); 
}

let form = document.forms.MyForm;
form.addEventListener('submit', processAndReturnValue);

function getRadius(e){
    e.preventDefault();
    return form.elements.radius.value;
}

function printVolumeOnPage(volume){
    form.elements.volume.value = volume;
}

function processAndReturnValue(e){
    let radius = getRadius(e);
    let volume = calculateVolume(radius);
    printVolumeOnPage(volume);
}
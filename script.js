document.getElementById("files").onchange = (e) => { 
    var file = e.target.files[0]; 
    var reader = new FileReader();
    reader.readAsText(file,'UTF-8');
    reader.onload = (readerEvent) => {
        var content = readerEvent.target.result;
        console.log(content);
    }
}
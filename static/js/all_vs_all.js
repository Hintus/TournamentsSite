function sizePic() {
    count = document.getElementById("size").value;
    box = document.getElementById("schema_box");

    box.style.width = `${25 * count+25}px`;

    var deleteElement = box.querySelectorAll('a');
    for (let i = 0; i < deleteElement.length; i++) {
        deleteElement[i].remove();
    }
    
    for(let i = 0; i<count; i++){
        for( j = 0;j<count ;j++){
            let div = document.createElement('a');
            if (i==j){
                div.className='cells_blocked'
            }else{
                div.className='cells'
            }
            box.append(div)
        }
    }
}
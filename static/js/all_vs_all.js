count = document.getElementById("size").value;
box = document.getElementById("schema_box");
document.getElementById("int_slider").value = count-1;

for(let i = 0; i<count; i++){
    for( j = 0;j<count ;j++){
        let div = document.createElement('a');
        div.id=`${i} ${j}`
        if (i==j){
            div.className='cells_blocked'
        }else{
            div.className='cells'
        }
        box.append(div)
    }
}


function sizePic() {
    count = document.getElementById("size").value;
    box = document.getElementById("schema_box");
    document.getElementById("int_slider").value = count-1;

    box.style.width = `${30 * count+30}px`;
    box.style.height = `${30 * count+30}px`;

    var deleteElement = box.querySelectorAll('a');
    for (let i = 0; i < deleteElement.length; i++) {
        deleteElement[i].remove();
    }
    
    for(let i = 0; i<count; i++){
        for( j = 0;j<count ;j++){
            let div = document.createElement('a');
            div.id=`${i} ${j}`
            if (i==j){
                div.className='cells_blocked'
            }else{
                div.className='cells'
            }
            box.append(div)
        }
    }
}
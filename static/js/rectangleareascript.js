addBtn = document.querySelector('#button_calculate');

addBtn.addEventListener('click',function(e){

    txtA = document.querySelector('#value_a');
    txtB = document.querySelector('#value_b');
    txtC = document.querySelector('#value_c');

    let c;

    c = parseFloat(txtA.value) * parseFloat(txtB.value);

    txtC.value = c;
});
let bgContainerE1 = document.createElement('div');
bgContainerE1.classList.add("bg-container");
document.body.appendChild(bgContainerE1);

let h1Element = document.createElement('h1');
h1Element.textContent = "Grocery List";
h1Element.classList.add("heading");
bgContainerE1.appendChild(h1Element);

let listcontainerE1 = document.createElement('ul');
listcontainerE1.classList.add('list-container');
bgContainerE1.appendChild(listcontainerE1);

let groceryItems = ["Milk", "Peanut Butter", "Choco Chips", "Tomato Sauce", "Cup Cakes", "Noodles"];
for (let item of groceryItems){
    let listItemE1 = document.createElement('li');
    listItemE1.textContent = item;
    listcontainerE1.appendChild(listItemE1);
}

let checkboxE1 = document.createElement('input');
checkboxE1.type = "checkbox";
checkboxE1.id = "deliveryMode";

bgContainerE1.appendChild(checkboxE1);

let labelE1 = document.createElement('label');
labelE1.setAttribute("for", "deliveryMode");
labelE1.classList.add("labelbox");
labelE1.textContent = "Need Home Delivery";

bgContainerE1.appendChild(labelE1);

let nextline = document.createElement('br');
bgContainerE1.appendChild(nextline);

let buttoninput = document.createElement('button');
buttoninput.classList.add('btn', "btn-primary");
buttoninput.textContent = "Proceed To Pay";

bgContainerE1.appendChild(buttoninput);
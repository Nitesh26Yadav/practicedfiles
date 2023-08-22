let todoItemsContainer = document.getElementById("todoItemsContainer");
let todoElement = document.createElement("li");
todoElement.classList.add("todo-item-container", "d-flex", "flex-row");
todoItemsContainer.appendChild(todoElement);

// Adding input statically.
// Creating input element and appending to todoelement.
let inputElement = document.createElement("input");
inputElement.type = "checkbox";
inputElement.id = "checkboxInput";
inputElement.classList.add("checkbox-input");
todoElement.appendChild(inputElement);

// Creating labelContainer and adding to TodoElement
let labelContainer = document.createElement("div");
labelContainer.classList.add("label-container", "d-flex", "flex-row");
todoElement.appendChild(labelContainer);

// Creating labelElement,giving set attribute, text Content and adding to labelcontainer.
let labelElement = document.createElement("label");
labelElement.setAttribute("for", "checkboxInput");
labelElement.classList.add("checkbox-label"); //Adding Class
labelElement.textContent = "Learn HTML";
labelContainer.appendChild(labelElement); 

// Creating deleteContainer and adding to labelContainer.
let deleteIconContainer = document.createElement("div");
deleteIconContainer.classList.add("delete-icon-container");
labelContainer.appendChild(deleteIconContainer);

// Creating deleteIcon and adding to delete Container.
let deleteIcon = document.createElement("i");
deleteIcon.classList.add("far", "fa-trash-alt", "delete-icon");
deleteIconContainer.appendChild(deleteIcon);


// Creating Multiple Todo Items:-
// Creating Reusable Function:

let todoList = [
    {
        text: "Learn HTML"
    },
    {
        text: "Learn CSS"
    },
    {
        text: "Learn JavaScript"
    }
]

function createAndappendTodo(todo) {
    let todoElement = document.createElement("li");
    todoElement.classList.add("todo-item-container", "d-flex", "flex-row");
    todoItemsContainer.appendChild(todoElement);

    // Creating input element and appending to todoelement.
    let inputElement = document.createElement("input");
    inputElement.type = "checkbox";
    inputElement.id = "checkboxInput";
    inputElement.classList.add("checkbox-input");
    todoElement.appendChild(inputElement);

    // Creating labelContainer and adding to TodoElement
    let labelContainer = document.createElement("div");
    labelContainer.classList.add("label-container", "d-flex", "flex-row");
    todoElement.appendChild(labelContainer);

    // Creating labelElement,giving set attribute, text Content and adding to labelcontainer.
    let labelElement = document.createElement("label");
    labelElement.setAttribute("for", "checkboxInput");
    labelElement.classList.add("checkbox-label"); //Adding Class
    labelElement.textContent = todo.text;
    labelContainer.appendChild(labelElement); 

    // Creating deleteContainer and adding to labelContainer.
    let deleteIconContainer = document.createElement("div");
    deleteIconContainer.classList.add("delete-icon-container");
    labelContainer.appendChild(deleteIconContainer);

    // Creating deleteIcon and adding to delete Container.
    let deleteIcon = document.createElement("i");
    deleteIcon.classList.add("far", "fa-trash-alt", "delete-icon");
    deleteIconContainer.appendChild(deleteIcon);
}


// createAndappendTodo(todoList[0]);
// createAndappendTodo(todoList[1]);
// createAndappendTodo(todoList[2]);

// using for of loop function to call todo text dynamically.
for (let todo of todoList) {
    createAndappendTodo(todo);
};
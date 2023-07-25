// alert('hi');

document.addEventListener('DOMContentLoaded', function()
{
    const addButton = document.querySelector('#add');
    const removeButton = document.querySelector('#remove');
    const view_list = document.querySelector('#view_list');
    // const buttons = document.querySelector('buttons')
    // buttons.forEach(function(button){
    //     button.onclick = function(){
    //         button.style.display = 'block';
    //     }

    // })
    const getButtons = document.querySelectorAll('.removeItems');
    const list = document.querySelector('#view_movies');
    const movieForm = document.querySelector('form');

    addButton.onclick = function(){
        if (list.style.display === 'block'){
            list.style.display = 'None';
        }
        movieForm.style.display = 'block';
        const addItem = document.querySelector('#addToDb');
        addItem.onclick = function(){
            const movieName = document.querySelector('#movieField').value;
            const platformName = document.querySelector('#platformField').value;
            alert(`Movie: ${movieName} on Platform: ${platformName} successfully added to list `)

        }
    }
    removeButton.onclick = function(){
        if (movieForm.style.display === 'block'){
            movieForm.style.display = 'None';
        }
        list.style.display = 'block';

        getButtons.forEach(function(button){
            button.style.display = 'block';
            button.onclick = function()
            {
                alert('Successfully removed the data from the list')
            }
        })


    }
    view_list.onclick = function(){
        const list = document.querySelector('#view_movies');
        list.style.display = 'block';
    }
})
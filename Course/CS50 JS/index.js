

person = {
    Name: 'Harry', 
    Last: 'Potter'
}
person.Name

if (!localStorage.getItem('counter')){
    localStorage.setItem('counter', 0)
}

document.addEventListener('DOMContentLoaded', function (){
    
    var dom = document.querySelector('h1');
    var sum = localStorage.getItem('counter');
    function count(dom)
    {
        sum++;
        dom.innerText = sum;     
        localStorage.setItem('counter', sum);
    }

    const button = document.querySelector('button');
    button.onclick = function(){
        count(dom);
    }
    // setInterval(count(dom), 1000);    // this function automatically does this
});

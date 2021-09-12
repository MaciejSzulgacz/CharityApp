let button = document.querySelector('#button');

button.addEventListener("click", function (event) {
    let categories = document.querySelector('#categories').value;
    let quantity = document.querySelector('#quantity').value;
    let organization = document.querySelector('#organization').value;
    let address = document.querySelector('#address').value;
    let city = document.querySelector('#city').value;
    let postcode = document.querySelector('#postcode').value;
    let phone = document.querySelector('#phone').value;
    let date = document.querySelector('#date').value;
    let time = document.querySelector('#time').value;
    let comments = document.querySelector('#comments').value;

    document.querySelector('#choosen_categories').innerHTML =
        `${quantity} worki ${categories} w dobrym stanie dla dzieci`;
    document.querySelector('#choosen_organization').innerHTML = `Dla fundacji ${organization} w Warszawie`;
    document.querySelector('#choosen_address').innerHTML = address;
    document.querySelector('#choosen_city').innerHTML = city;
    document.querySelector('#choosen_postcode').innerHTML = postcode;
    document.querySelector('#choosen_phone').innerHTML = phone;
    document.querySelector('#choosen_date').innerHTML = date;
    document.querySelector('#choosen_time').innerHTML = time;
    document.querySelector('#choosen_comments').innerHTML = comments;
});



document.addEventListener("DOMContentLoaded", function () {
  
  
    var addToCartBtn = document.getElementsByClassName("update-cart");
    for (var i = 0; i < addToCartBtn.length; i++) {
        addToCartBtn[i].addEventListener("click", function () {
        var productId = this.dataset.product;
        var action = this.dataset.action;
        console.log("productId", productId, "action", action);
        // alert("Product added")
        console.log(user);

        if (user === "AnonymousUser"){
            console.log("NOT LOGGED IN");
        }else{
            updateUserOrder(productId , action)
        }
    });
  }

  
function updateUserOrder(productId, action) {
    console.log("Item sent, logged in sending data");

    var url = '/update-item/';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'productId': productId, 'action': action})
    })
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        // console.log(data);
        location.reload();
    });
}

  
  
  // --------------Don't write code outside this 
});

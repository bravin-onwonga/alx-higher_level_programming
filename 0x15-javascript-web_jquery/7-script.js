$(function () {
  $.get("https://swapi-api.alx-tools.com/api/people/5/?format=json", function(res, status){
    if (status === "success") {
      $('DIV#character').text(res.name);
    } else {
      alert("I failed");
    }
  })
});

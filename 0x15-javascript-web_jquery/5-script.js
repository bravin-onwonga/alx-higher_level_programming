$(function () {
  $('DIV#add_item').click(function (event) {
    $('UL.my_list').append('<li>Item</li>');
  });
});

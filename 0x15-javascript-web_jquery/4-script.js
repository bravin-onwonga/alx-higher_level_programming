$(function () {
  $('DIV#toggle_header').click(function (event) {
    if (($('header').hasClass('green')) && ($('header').hasClass('red'))) {
      $('header').removeClass('red');
    } else if ($('header').hasClass('red')) {
      $('header').removeClass('red').addClass('green');
    } else if ($('header').hasClass('green')) {
      $('header').removeClass('green').addClass('red');
    } else {
      $('header').addClass('red');
    }
  });
});

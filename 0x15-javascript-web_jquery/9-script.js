$(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  $.get(url, function (res, status) {
    if (status === 'success') {
      $('DIV#hello').text((res.hello).translate({lang: "en"}));
    }
  });
});

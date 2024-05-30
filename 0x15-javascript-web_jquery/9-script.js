$(document).ready($(function () {
  function translateText (text, langto, dictionary) {
    if (dictionary[text] && dictionary[text][langto]) {
      return (dictionary[text][langto]);
    }
    return text;
  }

  const dict = { Salut: { en: 'Hello' } };
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  $.get(url, function (res, status) {
    if (status === 'success') {
      const translatedText = translateText(res.hello, 'en', dict);
      $('DIV#hello').text(translatedText);
    }
  });
}));

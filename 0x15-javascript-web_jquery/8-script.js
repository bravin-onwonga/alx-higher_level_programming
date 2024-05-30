$(function () {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.get(url, function (res, status) {
    if (status === 'success') {
      $.each(res.results, function (index, film) {
        $('UL#list_movies').append('<li>' + film.title + '</li>');
      });
    }
  });
});
